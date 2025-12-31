import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy

class XboxController(Node):
    def __init__(self):
        super().__init__('xbox_controller')
        self.sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        

    def joy_callback(self, msg):
        left_joystick_x= msg.axes[0]
        self.get_logger().info(f'{left_joystick_x}')

def main():
    rclpy.init()
    xbox_controller = XboxController()
    try:
        rclpy.spin(xbox_controller)
    except KeyboardInterrupt:
        xbox_controller.destroy_node()
        rclpy.shutdown()
    

if __name__ == '__main__':
    main()