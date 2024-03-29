# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/kinetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/kinetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in "/home/pi/catkin_ws_1/devel_isolated/rosmaster;/home/pi/catkin_ws_1/devel_isolated/roslz4;/home/pi/catkin_ws_1/devel_isolated/roslaunch;/home/pi/catkin_ws_1/devel_isolated/rosgraph;/home/pi/catkin_ws_1/devel_isolated/ros_comm;/home/pi/catkin_ws_1/devel_isolated/mpu_6050_driver;/home/pi/catkin_ws_1/devel_isolated/image_common;/home/pi/catkin_ws_1/devel;/opt/ros/kinetic".split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/pi/catkin_ws_1/devel_isolated/rosparam/env.sh')

output_filename = '/home/pi/catkin_ws_1/build_isolated/rosparam/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    #print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
