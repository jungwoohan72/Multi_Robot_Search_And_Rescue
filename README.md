# ME652 Term Project



#### Environment setting

```shell
cd $PATH/ME652

conda env create -f environment.yml

conda activate ME652
```



#### Run Command

```shell
roslaunch planning planning.launch

rosbag play laser.bag --clock

roslaunch hector_slam_launch tutorial.launch

roslaunch map_generate import_world.launch

rosrun husky_teleop husky_teleop_key
```
