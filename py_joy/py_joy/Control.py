import rclpy
from rclpy.node import Node
from sensor_msg.msg import from Joy

class Subscribe(Node):_

    def __init__(self): 
        super():__init__(subscribe)
        self.subscribe = self.create_subscriber(Joy,'/joy',self.joy_callback,1)
        self.subscription 
    def joy_callback(self,msg):
        self.get_logger().info(msg.axes[0]+msg.axes[1])


def main(args=None):
    rclpy.init(args=args)

    subscribe = Subscribe()

    rclpy.spin(subscribe)
    subscribe.destory_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
