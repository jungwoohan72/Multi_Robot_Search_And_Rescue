# Install script for directory: /home/morin-sol/ME652/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/morin-sol/ME652/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/morin-sol/ME652/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/morin-sol/ME652/install" TYPE PROGRAM FILES "/home/morin-sol/ME652/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/morin-sol/ME652/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/morin-sol/ME652/install" TYPE PROGRAM FILES "/home/morin-sol/ME652/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/morin-sol/ME652/install/setup.bash;/home/morin-sol/ME652/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/morin-sol/ME652/install" TYPE FILE FILES
    "/home/morin-sol/ME652/build/catkin_generated/installspace/setup.bash"
    "/home/morin-sol/ME652/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/morin-sol/ME652/install/setup.sh;/home/morin-sol/ME652/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/morin-sol/ME652/install" TYPE FILE FILES
    "/home/morin-sol/ME652/build/catkin_generated/installspace/setup.sh"
    "/home/morin-sol/ME652/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/morin-sol/ME652/install/setup.zsh;/home/morin-sol/ME652/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/morin-sol/ME652/install" TYPE FILE FILES
    "/home/morin-sol/ME652/build/catkin_generated/installspace/setup.zsh"
    "/home/morin-sol/ME652/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/morin-sol/ME652/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/morin-sol/ME652/install" TYPE FILE FILES "/home/morin-sol/ME652/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/morin-sol/ME652/build/gtest/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/geometry2/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_geotiff_launch/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_slam/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_slam_launch/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/navigation/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation_msgs/move_base_msgs/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_map_tools/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_nav_msgs/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2_msgs/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2_bullet/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2_eigen/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_geotiff/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_geotiff_plugins/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_marker_drawing/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/husky_teleop/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/planning/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/map_server/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2_py/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_compressed_map_transport/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation_msgs/map_msgs/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2_ros/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_imu_attitude_to_tf/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_imu_tools/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_map_server/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_trajectory_server/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/map_generate/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2_geometry_msgs/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/amcl/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/fake_localization/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/hector_slam/hector_mapping/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/ira_laser_tools/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/m-explore/map_merge/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2_kdl/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/test_tf2/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2_sensor_msgs/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/geometry2-melodic-devel/tf2_tools/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/voxel_grid/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/costmap_2d/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/m-explore/explore/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/nav_core/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/base_local_planner/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/carrot_planner/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/clear_costmap_recovery/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/dwa_local_planner/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/move_slow_and_clear/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/navfn/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/global_planner/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/rotate_recovery/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/navigation/move_base/cmake_install.cmake")
  include("/home/morin-sol/ME652/build/husky_description/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/morin-sol/ME652/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
