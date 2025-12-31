import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class XboxReader(Node):
    def __init__(self):
        super().__init__('xbox_reader')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'joy_data',
            self.listener_callback,
            10
        )
        self.get_logger().info('Xbox Reader has been started.')
        self.subscription  # prevents unused variable warning

    def listener_callback(self, msg):
        x_axis, y_axis = msg.data
        self.get_logger().info(f'Received X: {x_axis:.2f}, Y: {y_axis:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = XboxReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()