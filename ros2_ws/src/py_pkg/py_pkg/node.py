import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class JoystickPublisher(Node):

    def __init__(self):
        super().__init__('joystick_publisher')
        self.subscription = self.create_subscription(Joy, "joy", self.listener_callback, 10)

    def listener_callback(self, msg):
        x = msg.axes[0]
        y = msg.axes[1]
        self.get_logger().info(f'X-Axis: {x:.2f}, Y-Axis: {y:.2f}')

def main(args=None):
    rclpy.init(args=args)
    joystick_publisher = JoystickPublisher()
    rclpy.spin(joystick_publisher)
    joystick_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()