execute_process(COMMAND "/home/morin-sol/ME652/build/husky_teleop/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/morin-sol/ME652/build/husky_teleop/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
