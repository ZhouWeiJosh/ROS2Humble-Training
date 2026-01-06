import rclpy
from rclpy.node import Node

# Message datatype for joystick data
# Refer to https://docs.ros2.org/latest/api/sensor_msgs/msg/Joy.html
from sensor_msgs.msg import Joy

class XboxController(Node):
    def __init__(self):
        # Initialize the ROS 2 node with the name "xbox_controller"
        super().__init__('xbox_controller')

        # Create a subscription to the /joy topic
        # - Message type: Joy
        # - Topic name: /joy
        # - Callback function: self.joy_callback
        # - Queue size: 10
        # I formated it like this to be explicit about the parameters
        self.sub = self.create_subscription(msg_type = Joy, 
                                            topic = '/joy', 
                                            callback = self.joy_callback,
                                            qos_profile = 10)
        
        # Can also just do this:
        # self.sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
    # Callback are functions that get called when a new message is received from the 
    # subscribed topic while the node is "spinning"
    def joy_callback(self, msg):
        # Read the X-axis value of the left joystick
        # Axis indices are controller-dependent; for Xbox controllers,
        # axes[0] is typically the left joystick X-axis
        left_joystick_x= msg.axes[0]
        self.get_logger().info(f'{left_joystick_x}')

def main():
    # Initialize the ROS 2 Python client library 
    # Need this for any ROS 2 Python program
    rclpy.init()

    # Create an instance of the XboxController node
    xbox_controller = XboxController()

    try:
        # Keep the node alive and processing callbacks
        rclpy.spin(xbox_controller)
    except KeyboardInterrupt:
        # Gracefully shut down on Ctrl+C
        xbox_controller.destroy_node()
        rclpy.shutdown()
    
# Standard Python entry point
if __name__ == '__main__':
    main()