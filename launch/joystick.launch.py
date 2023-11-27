from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, EnvironmentVariable
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    joy_params = os.path.join(get_package_share_directory('my_bot'),'config','joystick.yaml')

<<<<<<< HEAD
    # joy_node = Node(
    #         package='joy',
    #         executable='joy_node',
    #         parameters=[joy_params],
    #      )
=======
    joy_node = Node(
            package='joy',
            executable='joy_node',
            parameters=[joy_params, {'use_sim_time': use_sim_time}]
         )
>>>>>>> 4b25a21f8fc6c94daf4c0159a972fe023c262273

    teleop_node = Node(
            package='teleop_twist_joy', 
            executable='teleop_node',
            name = 'teleop_node',
            parameters=[joy_params, {'use_sim_time': use_sim_time}],
            remappings=[('/cmd_vel', '/diff_cont/cmd_vel_unstamped')]
            )
    
    # twist_stamper = Node(
    #     package='twist_stamper',
    #     executable='twist_stamper',
    #     parameters=[{'use_sim_time': use_sim_time}],
    #     remappings=[('/cmd_vel_in','/diff_cont/cmd_vel_unstamped'),
    #                 ('/cmd_vel_out','/diff_cont/cmd_vel')]
    #   )
    

    return LaunchDescription([
<<<<<<< HEAD
        # joy_node,
        teleop_node     
=======
            DeclareLaunchArgument(
                'use_sim_time',
                default_value='false',
                description='Use sim time if true'),
        joy_node,
        teleop_node,
        # twist_stamper     
>>>>>>> 4b25a21f8fc6c94daf4c0159a972fe023c262273
    ])