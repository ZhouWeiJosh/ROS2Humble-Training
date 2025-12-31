import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32MultiArray

class JoyNode(Node):
    def __init__(self):
        super().__init__('joy')
        self.publisher_ = self.create_publisher(Float32MultiArray, '/joy_data', 10)
        self.get_logger().info('Joy Node has been started.')

    def joy_callback(self, msg):
        x_axis = msg.axes[0]
        y_axis = msg.axes[1]

        axes_msg = Float32MultiArray()
        axes_msg.data = [x_axis, y_axis]
        self.publisher_.publish(axes_msg)

        self.get_logger().info(
            f'Sending X: {x_axis:.2f}, Y: {y_axis:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = JoyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()