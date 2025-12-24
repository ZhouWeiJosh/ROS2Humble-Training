#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

from std_msgs.msg import String

class JoySubscriber(Node):

    def __init__(self):
        super().__init__('joy_subscriber')
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.listener_callback,
            10)
    def listener_callback(self, msg):
        self.get_logger().info('X axes: "%s"' % msg.axes[0] + ' Y axes: "%s"' % msg.axes[1])
    
def main(args=None):
    rclpy.init(args=args)

    joy_subscriber = JoySubscriber()

    rclpy.spin(joy_subscriber)

    joy_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()