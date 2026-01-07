from setuptools import find_packages, setup
import os
from glob import glob   

package_name = 'xbox_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rav3z',
    maintainer_email='corp.rvn@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'joy = xbox_controller.joy:main',
        'xbox_reader = xbox_controller.xbox_reader:main',
        'xbox_logger = xbox_controller.xbox_logger:main',
        ],
    },
)
