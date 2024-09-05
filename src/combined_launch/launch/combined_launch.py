from launch import LaunchDescription
from launch_ros.actions import Node
import launch
import launch.actions
import launch_ros.actions

def generate_launch_description():
    # 启动 usb_cam 的节点
    usb_cam_launch = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource([
            launch.substitutions.PathJoinSubstitution([
                launch.substitutions.FindPackageShare('usb_cam'),
                'launch',
                'camera.launch.py'
            ])
        ])
    )

    # 启动 web_video_server 的节点
    web_video_server_launch = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource([
            launch.substitutions.PathJoinSubstitution([
                launch.substitutions.FindPackageShare('web_video_server_ros2'),
                'launch',
                'web_video_server_launch.py'
            ])
        ])
    )

    # 返回 LaunchDescription 并包含两个功能包的启动
    return LaunchDescription([
        usb_cam_launch,
        web_video_server_launch,
    ])
