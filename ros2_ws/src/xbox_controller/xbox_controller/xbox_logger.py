import rclpy
from rclpy.node import Node

# Refer to https://docs.ros2.org/latest/api/std_msgs/msg/Int8.html
from std_msgs.msg import Int32

class XboxLogger(Node):
    def __init__(self):
        # Initialize the ROS 2 node with the name "xbox_logger"
        super().__init__('xbox_logger')

        ''' 
        Create a subscription to the /button_a_press topic
        - Message type: Joy
        - Topic name: /joy
        - Callback function: self.button_a_press_callback
        - Queue size: 10
        '''
        self.create_subscription(Int32, '/button_a_press', self.button_a_press_callback, 10)

    def button_a_press_callback(self, msg):
        if msg.data == 1:
            self.get_logger().info(f'Button A is being pressed yippie')
        else:
            self.get_logger().info(f'Button A is not being pressed :(')

def main():
    rclpy.init()

    xbox_logger = XboxLogger()

    try: 
        rclpy.spin(xbox_logger)
    except KeyboardInterrupt:
        xbox_logger.destroy_node
        rclpy.shutdown

if __name__ == '__main__':
    main()

    