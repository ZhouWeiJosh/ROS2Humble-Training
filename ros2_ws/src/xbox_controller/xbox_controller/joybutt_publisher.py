#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

from std_msgs.msg import Int32
from std_msgs.msg import String


class ButtonPublisher(Node):
    def __init__(self):

        super().__init__('button_a_press')
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.listener_callback,
            10
            )

        
        self.publisher_ = self.create_publisher (Int32,'button_a_press',10)
 

    def listener_callback(self, msg):
        self.publisher_.publish(Int32(data = msg.buttons[0]))
        self.get_logger().info(f"Publishing: {msg.buttons[0]}")
        



def main(args = None):
    rclpy.init(args = args)

    button_publisher = ButtonPublisher()

    rclpy.spin(button_publisher)

    rclpy.shutdown()

if __name__ == '__main__':
    main()

        