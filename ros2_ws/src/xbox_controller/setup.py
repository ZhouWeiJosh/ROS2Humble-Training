from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'xbox_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jorda',
    maintainer_email='jxiong@hawaii.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
           'joynode_subscriber = xbox_controller.joynode_subscriber:main',
           'joybutt_publisher = xbox_controller.joybutt_publisher:main',
           'xbox_logger = xbox_controller.xbox_logger:main',
        ],
    },
)
