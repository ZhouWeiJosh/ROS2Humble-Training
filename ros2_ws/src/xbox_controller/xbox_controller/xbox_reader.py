#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy


class XboxReader(Node):
    def __init__(self):
        super().__init__('xbox_reader')

        # /joy publishes sensor_msgs/Joy
        self.sub = self.create_subscription(Joy, '/joy', self.cb, 10)

        # Typical mapping (varies by controller/driver):
        # axes[0] = left stick left/right (X)
        # axes[1] = left stick up/down   (Y)
        self.left_x_index = 0
        self.left_y_index = 1

        self.get_logger().info('Subscribed to /joy. Printing left stick X/Y...')

    def cb(self, msg: Joy):
        # Guard in case axes array is smaller than expected
        if len(msg.axes) <= max(self.left_x_index, self.left_y_index):
            self.get_logger().warn(f"Joy axes too short: len={len(msg.axes)}")
            return

        lx = msg.axes[self.left_x_index]
        ly = msg.axes[self.left_y_index]

        # Print to terminal
        self.get_logger().info(f"Left stick: X={lx:.3f}, Y={ly:.3f}")


def main():
    rclpy.init()
    node = XboxReader()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
