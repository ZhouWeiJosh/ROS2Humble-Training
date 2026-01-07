import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class XboxReader(Node):
    def __init__(self):
        super().__init__('xbox_logger')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'button_a_press',
            self.listener_callback,
            10
        )
        self.get_logger().info('Xbox Logger has been started.')
        self.subscription  # prevents unused variable warning

    def listener_callback(self, msg):
        button_a = msg.data[0]
        self.get_logger().info(f'Received Button A Press: {button_a}')

def main(args=None):
    rclpy.init(args=args)
    node = XboxReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()