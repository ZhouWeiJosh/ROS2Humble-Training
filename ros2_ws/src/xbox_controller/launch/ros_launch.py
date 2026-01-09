from launch import LaunchDescription
from launch_ros.actions import Node 

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
        ),
        Node(
            package='xbox_controller',
            executable='joybutt_publisher',
            name='joybutt_publisher_node',
            output='screen',
        ),
        Node(
            package='xbox_controller',
            executable='xbox_logger',
            name='xbox_logger_node',
            output='screen',
        ),
    ])