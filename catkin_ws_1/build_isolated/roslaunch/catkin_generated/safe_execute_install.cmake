execute_process(COMMAND "/home/pi/catkin_ws_1/build_isolated/roslaunch/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/pi/catkin_ws_1/build_isolated/roslaunch/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
