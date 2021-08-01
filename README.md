# ME652 Term Project

## Scenario environment

Unstructured post-disaster Search-And-Rescue (SAR) envionment in Gazebo.

<img width="613" alt="Map_post_disaster" src="https://user-images.githubusercontent.com/45442859/127759892-9503578c-8497-48d1-8b04-099ecb34d5e6.png">

## Scenario

Three autonomous mobile robots simultaneously head toward the possible search point by performing real-time Hector-SLAM and D* Lite path planning. In this process, each robot shares its constructed map information with the other robots to efficiently map the global environment.

<img width="613" alt="스크린샷 2021-08-01 오후 2 01 42" src="https://user-images.githubusercontent.com/45442859/127759823-313924bb-7fb9-4e6e-94a2-800b86de6eec.png">
<img width="613" alt="스크린샷 2021-08-01 오후 2 02 19" src="https://user-images.githubusercontent.com/45442859/127759829-b7aa18b0-443e-4562-a956-dd0037ad2281.png">

## Demo video

![나의 동영상 1](https://user-images.githubusercontent.com/45442859/127759969-299a5173-b8be-447d-95ea-b99c9a413fc9.gif)

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
