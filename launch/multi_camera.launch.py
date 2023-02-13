from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='multi_camera_pkg',
            namespace='camera_1',
            executable='camera_1',
            name='sim'
        ),
        Node(
            package='multi_camera_pkg',
            namespace='camera_2',
            executable='camera_2',
            name='sim'
        ),
        Node(
            package='multi_camera_pkg',
            namespace='camera_3',
            executable='camera_3',
            name='sim'
        )
    ])