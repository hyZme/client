# CMake generated Testfile for 
# Source directory: /home/pi/catkin_ws_1/src/image_common/camera_info_manager
# Build directory: /home/pi/catkin_ws_1/build_isolated/camera_info_manager
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_camera_info_manager_rostest_tests_unit_test.test "/home/pi/catkin_ws_1/build_isolated/camera_info_manager/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/pi/catkin_ws_1/build_isolated/camera_info_manager/test_results/camera_info_manager/rostest-tests_unit_test.xml" "--return-code" "/opt/ros/kinetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/pi/catkin_ws_1/src/image_common/camera_info_manager --package=camera_info_manager --results-filename tests_unit_test.xml --results-base-dir \"/home/pi/catkin_ws_1/build_isolated/camera_info_manager/test_results\" /home/pi/catkin_ws_1/src/image_common/camera_info_manager/tests/unit_test.test ")
subdirs("gtest")
