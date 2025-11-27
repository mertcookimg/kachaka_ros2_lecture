# Kachaka ROS2 Lecture

This is a lecture/educational repository that demonstrates various ROS2 functionalities with the Kachaka robot.

Kachakaロボットを使用したROS2の様々な機能を実演する講義・教育用リポジトリです。

More lecture information: https://mertcookimg.github.io/ros2_lecture/

## Prerequisites / 前提条件
- ROS2 Humble
- Kachaka robot with API enabled / APIが有効なKachakaロボット

## Packages Overview / パッケージ概要

### Core Kachaka Packages from [Kachaka API](https://github.com/pf-robotics/kachaka-api) / Kachaka APIからのコアパッケージ
These packages are provided by the official Kachaka API repository:
公式のKachaka APIリポジトリから提供されるパッケージ：
- `kachaka_description`([Original Repository](https://github.com/pf-robotics/kachaka-api)): Robot description and URDF files / ロボットの記述とURDFファイル
- `kachaka_interfaces`([Original Repository](https://github.com/pf-robotics/kachaka-api)): ROS2 message and service definitions / ROS2メッセージとサービス定義
- `kachaka_nav2_bringup`([Original Repository](https://github.com/pf-robotics/kachaka-api)): Navigation2 configuration and launch files / Navigation2の設定とlaunchファイル
- `kachaka_speak`([Original Repository](https://github.com/pf-robotics/kachaka-api)): ROS2 speech synthesis package / ROS2音声合成パッケージ

### Control Packages / 制御パッケージ
Custom packages developed for this lecture:
この講義用に開発されたカスタムパッケージ：
- `kachaka_feedforward_control`: Feedforward control implementation / フィードフォワード制御の実装
- `kachaka_feedback_control`: Feedback control implementation / フィードバック制御の実装
- `kachaka_lidar_control`: LiDAR sensor control and processing / LiDARセンサーの制御と処理

### Image Processing Packages / 画像処理パッケージ
Custom packages developed for this lecture:
この講義用に開発されたカスタムパッケージ：
- `image_gray_processor`: Grayscale image processing / グレースケール画像処理
- `image_edge_detection`: Edge detection algorithms / エッジ検出アルゴリズム
- `image_yolo_detection`: YOLO-based object detection / YOLOベースの物体検出

### Teleoperation Packages / 遠隔操作パッケージ
- `teleop_twist_keyboard` ([Original Repository](https://github.com/ros2/teleop_twist_keyboard)): Keyboard teleoperation node for ROS2 / ROS2用キーボード遠隔操作ノード

### Integration Packages / 統合パッケージ
- `kachaka_speak_detection`: Speech detection and recognition package / 音声検出と認識パッケージ

## License Information / ライセンス情報

| Package Category / パッケージカテゴリ | License Type / ライセンスタイプ | Description / 説明 |
|-----------------|--------------|-------------|
| Kachaka Packages / Kachakaパッケージ | Apache License 2.0 | Core Kachaka packages from official API / 公式APIからのコアKachakaパッケージ |
| Control Packages / 制御パッケージ | Apache License 2.0 | Custom control packages for this lecture / この講義用のカスタム制御パッケージ |
| Image Processing / 画像処理 | Apache License 2.0 | Custom image processing packages / カスタム画像処理パッケージ |
| Teleoperation / 遠隔操作 | BSD License 2.0 | teleop_twist_keyboard |
| Integration / 統合 | Apache License 2.0 | Custom integration packages / カスタム統合パッケージ |

For detailed license information and copyright notices, please refer to individual package directories.
詳細なライセンス情報と著作権表示については、各パッケージディレクトリを参照してください。

## Building and Usage / ビルドと使用方法

1. Make sure you have ROS2 installed / ROS2がインストールされていることを確認してください
2. Clone this repository / このリポジトリをクローンしてください
3. Build the workspace / ワークスペースをビルドしてください

## How to Use / 使い方

More lecture information: https://mertcookimg.github.io/ros2_lecture/

## Acknowledgments / 謝辞

- [Preferred Robotics, Inc.](https://github.com/pf-robotics) for the Kachaka robot and API / KachakaロボットとAPIを開発してくださったPreferred Robotics, Inc.
- ROS2 community for the teleop_twist_keyboard package / teleop_twist_keyboardパッケージを提供してくださったROS2コミュニティ

