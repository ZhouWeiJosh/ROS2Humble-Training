#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class XboxLogger(Node):

    def __init__(self):
        super().__init__('xbox_logger')
        self.subscription = self.create_subscription(
            Int32,
            'button_a_press',
            self.listener_callback,
            10
            )
            
        

    def listener_callback(self, msg):
        self.get_logger().info(f"Button A {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    xbox_logger = XboxLogger()

    rclpy.spin(xbox_logger)

    xbox_logger.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()