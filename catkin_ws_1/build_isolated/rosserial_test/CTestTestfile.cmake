# CMake generated Testfile for 
# Source directory: /home/pi/catkin_ws_1/src/rosserial/rosserial_test
# Build directory: /home/pi/catkin_ws_1/build_isolated/rosserial_test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_rosserial_test_rostest_test_rosserial_server_socket.test "/home/pi/catkin_ws_1/build_isolated/rosserial_test/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/pi/catkin_ws_1/build_isolated/rosserial_test/test_results/rosserial_test/rostest-test_rosserial_server_socket.xml" "--return-code" "/opt/ros/kinetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/pi/catkin_ws_1/src/rosserial/rosserial_test --package=rosserial_test --results-filename test_rosserial_server_socket.xml --results-base-dir \"/home/pi/catkin_ws_1/build_isolated/rosserial_test/test_results\" /home/pi/catkin_ws_1/src/rosserial/rosserial_test/test/rosserial_server_socket.test ")
add_test(_ctest_rosserial_test_rostest_test_rosserial_server_serial.test "/home/pi/catkin_ws_1/build_isolated/rosserial_test/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/pi/catkin_ws_1/build_isolated/rosserial_test/test_results/rosserial_test/rostest-test_rosserial_server_serial.xml" "--return-code" "/opt/ros/kinetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/pi/catkin_ws_1/src/rosserial/rosserial_test --package=rosserial_test --results-filename test_rosserial_server_serial.xml --results-base-dir \"/home/pi/catkin_ws_1/build_isolated/rosserial_test/test_results\" /home/pi/catkin_ws_1/src/rosserial/rosserial_test/test/rosserial_server_serial.test ")
add_test(_ctest_rosserial_test_rostest_test_rosserial_python_socket.test "/home/pi/catkin_ws_1/build_isolated/rosserial_test/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/pi/catkin_ws_1/build_isolated/rosserial_test/test_results/rosserial_test/rostest-test_rosserial_python_socket.xml" "--return-code" "/opt/ros/kinetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/pi/catkin_ws_1/src/rosserial/rosserial_test --package=rosserial_test --results-filename test_rosserial_python_socket.xml --results-base-dir \"/home/pi/catkin_ws_1/build_isolated/rosserial_test/test_results\" /home/pi/catkin_ws_1/src/rosserial/rosserial_test/test/rosserial_python_socket.test ")
subdirs("gtest")
