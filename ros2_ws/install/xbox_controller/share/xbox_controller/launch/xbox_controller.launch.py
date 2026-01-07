from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='xbox_controller',
            executable='joy',
            name='joy_node',
        ),
        Node(
            package='xbox_controller',
            executable='xbox_reader',
            name='reader',
        ),
        Node(
            package='xbox_controller',
            executable='xbox_logger',
            name='logger',
        ),  
    ])