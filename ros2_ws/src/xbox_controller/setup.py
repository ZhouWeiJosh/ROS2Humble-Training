import os

from setuptools import find_packages, setup

package_name = 'xbox_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    # Changed this for launch file
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/xbox_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lzheng',
    maintainer_email='zheng3@hawaii.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    # Added a console script entry point to be able to ROS2 run the node
    entry_points={
        'console_scripts': [
            'xbox_controller = xbox_controller.xbox_controller:main'
        ],
    },
)
