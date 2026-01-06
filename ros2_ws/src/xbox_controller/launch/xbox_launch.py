from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    launch_description = LaunchDescription()

    launch_description.add_action(
        Node(
        package = 'joy',
        executable = 'joy_node',
        name = 'joy_node'
        )
    )

    launch_description.add_action(
        Node(
            package='xbox_controller',
            executable='xbox_controller',
            name='xbox_controller'
        )
    )

    launch_description.add_action(
        Node(
            package='xbox_controller',
            executable='xbox_logger',
            name='xbox_logger'
        )
    )

    return launch_description