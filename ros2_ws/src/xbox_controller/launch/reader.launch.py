from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='xbox_controller',
            executable='reader',
            name='xbox_reader',
            output='screen',
        )
    ])
