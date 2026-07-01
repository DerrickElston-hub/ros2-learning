from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    # Get the path to the URDF file
    urdf_file = os.path.join(
        get_package_share_directory('my_robot_description'),
        'urdf',
        'inspection_robot.urdf'
    )

    # Read the URDF file
    with open(urdf_file, 'r') as file:
        robot_description = file.read()

    return LaunchDescription([

        # Publish the robot model (TF tree)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[
                {
                    'robot_description': robot_description
                }
            ]
        ),

        # GUI for moving robot joints
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        # Start RViz
        Node(
            package='rviz2',
            executable='rviz2'
        )

    ])