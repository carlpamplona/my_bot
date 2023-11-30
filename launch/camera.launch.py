import os
 
from launch import LaunchDescription
from launch_ros.actions import Node
 
def generate_launch_description():
 
 
 
    return LaunchDescription([
 
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen',
            parameters=[{
                'image_size': [640,480],
                'camera_frame_id': 'camera_link_optical'
                }]
        )
    ])

    # return LaunchDescription([
 
    #    Node(
    #         package='usb_cam',
    #         executable='usb_cam_node_exe',
    #         name='usb_cam',
    #         output='screen',
    #         parameters=[
    #             {'video_device': '/dev/video1',  # Set the correct path for your USB HD camera
    #             'image_width': 640,
    #             'image_height': 480,
    #             'camera_frame_id': 'camera_link_optical',
    #             'pixel_format': 'yuyv',
    #             'camera_info_url': '',
    #             'auto_focus': False,
    #             'camera_info_url': ''}  # Add any other parameters you need
    #         ],
    #     )
    # ])