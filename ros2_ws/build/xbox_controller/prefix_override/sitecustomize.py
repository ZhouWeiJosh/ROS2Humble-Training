import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jadoom/ROS2Humble-Training/ros2_ws/install/xbox_controller'
