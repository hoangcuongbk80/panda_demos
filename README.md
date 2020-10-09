## Install
Require full ROS installation. The installation assumes you have Ubuntu 16.04 LTS [ROS Kinetic]
1. install franka_ros from source first: https://github.com/tstoyanov/franka_ros.git
2. then install this repo: https://github.com/hoangcuongbk80/panda_demos.git
3. sudo apt-get install ros-kinetic-joint-state-controller
4. sudo apt install ros-kinetic-moveit
5. sudo apt-get install ros-kinetic-ros-control* ros-kinetic-gazebo-ros-control

## To run:
roslaunch panda_table_description panda_gazebo_effort.launch <br/>
rosrun grasp_detection pick_place_node (from another terminal)
