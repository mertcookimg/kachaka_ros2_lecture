#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import numpy as np
from tf_transformations import euler_from_quaternion

# Imports for QoS settings
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

class KachakaFeedbackControl(Node):
    def __init__(self):
        super().__init__('kachaka_feedback_control')

        # Declare parameter to check if running in simulation
        self.declare_parameter('use_sim', False)
        use_sim = self.get_parameter('use_sim').get_parameter_value().bool_value

        # Define a QoS profile with BEST_EFFORT reliability
        qos_profile = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10,
            reliability=QoSReliabilityPolicy.BEST_EFFORT
        )

        # Publisher for velocity commands
        self.cmd_vel_pub = self.create_publisher(Twist, '/kachaka/manual_control/cmd_vel', 10)

        # Select odometry topic based on simulation mode
        if use_sim:
            odom_topic = '/kachaka/wheel_odometry/wheel_odometry'
        else:
            odom_topic = '/kachaka/odometry/odometry'

        # Subscriber for odometry data with BEST_EFFORT QoS
        self.odom_sub = self.create_subscription(
            Odometry,
            odom_topic,
            self.callback_odom,
            qos_profile
        )
        
        self.get_logger().info(f'Subscribing to odometry topic: {odom_topic}')

        self.x = None
        self.y = None
        self.yaw = None

        # Wait for the first odometry message to be received
        while self.x is None or self.y is None or self.yaw is None:
            rclpy.spin_once(self, timeout_sec=0.1)

    def callback_odom(self, msg):
        """Callback function for receiving odometry data."""
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.yaw = self.get_yaw_from_quaternion(msg.pose.pose.orientation)

    def get_yaw_from_quaternion(self, quaternion):
        # Convert quaternion to Euler angles and return the yaw
        e = euler_from_quaternion((quaternion.x, quaternion.y, quaternion.z, quaternion.w))
        return e[2]

    def go_straight(self, distance, velocity=0.3):
        """
        Move straight for the specified distance.
        """
        vel = Twist()
        x0 = self.x
        y0 = self.y
        while np.sqrt((self.x - x0)**2 + (self.y - y0)**2) < distance:
            vel.linear.x = velocity
            vel.angular.z = 0.0
            self.cmd_vel_pub.publish(vel)
            rclpy.spin_once(self, timeout_sec=0.1)
        self.stop()

    def turn_right(self, angle_degree, yawrate=-0.5):
        """
        Turn right by the specified angle (in degrees) using a negative yaw rate.
        """
        vel = Twist()
        yaw0 = self.yaw
        target_angle = math.radians(angle_degree)
        # Normalize the angle difference using atan2
        while abs(math.atan2(math.sin(self.yaw - yaw0), math.cos(self.yaw - yaw0))) < target_angle:
            vel.linear.x = 0.0
            vel.angular.z = yawrate
            self.cmd_vel_pub.publish(vel)
            rclpy.spin_once(self, timeout_sec=0.1)
        self.stop()

    def turn_left(self, angle_degree, yawrate=0.5):
        """
        Turn left by the specified angle (in degrees) using a positive yaw rate.
        """
        vel = Twist()
        yaw0 = self.yaw
        target_angle = math.radians(angle_degree)
        # Normalize the angle difference using atan2
        while abs(math.atan2(math.sin(self.yaw - yaw0), math.cos(self.yaw - yaw0))) < target_angle:
            vel.linear.x = 0.0
            vel.angular.z = yawrate
            self.cmd_vel_pub.publish(vel)
            rclpy.spin_once(self, timeout_sec=0.1)
        self.stop()

    def stop(self):
        """Stop the robot by publishing zero velocities."""
        vel = Twist()
        vel.linear.x = 0.0
        vel.angular.z = 0.0
        self.cmd_vel_pub.publish(vel)

def main(args=None):
    rclpy.init(args=args)
    kachaka_feedback_control = KachakaFeedbackControl()

    try:
        # Example movement commands: go straight, turn left, then turn right
        kachaka_feedback_control.go_straight(1.0)
        kachaka_feedback_control.turn_left(90)
        kachaka_feedback_control.turn_right(90)
    finally:
        kachaka_feedback_control.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()