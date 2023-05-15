from setuptools import setup

package_name = 'webots_ros2_crazyflie'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/worlds', [
    'worlds/crazyflie_simple_world.wbt', 'worlds/.crazyflie_simple_world.wbproj',
]))
data_files.append(('share/' + package_name + '/resource', [
    'resource/crazyflie_webots.urdf'
]))

setup(
    name=package_name,
    version='2023.0.3',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    author='Kimberly McGuire',
    author_email='kimberly@bitcraze.io',
    maintainer='Kimberly McGuire',
    maintainer_email='kimberly@bitcraze.io',
    description='The Webots ROS 2 package for the Crazyflie',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'crazyflie_driver = webots_ros2_crazyflie.crazyflie_driver:main'
        ],
    },
)
