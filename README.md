# ME652 Term Project



#### Environment setting

```shell
cd $PATH/ME652

conda env create -f environment.yml

conda activate ME652
```



#### Run Command

```shell
roslaunch hector_slam_launch slam.launch

roslaunch map_generate import_world.launch

roslaunch planning planning.launch

rosrun husky_teleop husky_teleop_key
```
