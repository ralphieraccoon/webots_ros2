from setuptools import setup

package_name = 'webots_ros2_crazyflie'

setup(
    name=package_name,
    version='2023.0.3',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    author='Kimberly McGuire',
    author_email='kimberly@bitcraze.io',
    maintainer='Kimberly McGuire',
    maintainer_email='kimberly@bitcraze.io',
    description='The Webots ROS2 package for the Crazyflie',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'crazyflie_driver = webots_ros2_crazyflie.crazyflie_driver:main'
        ],
    },
)
