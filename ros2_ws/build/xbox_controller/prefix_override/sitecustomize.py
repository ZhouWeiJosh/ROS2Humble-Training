import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rav3z/ROS2Humble-Training/ros2_ws/install/xbox_controller'
