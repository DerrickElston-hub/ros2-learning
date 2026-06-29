from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='my_first_package',
            executable='inspection_camera_node',
            name='inspection_camera_node'
        ),

        Node(
            package='my_first_package',
            executable='inspection_node',
            name='inspection_node'
        ),

        Node(
            package='my_first_package',
            executable='inspection_service',
            name='inspection_service'
        )

    ])