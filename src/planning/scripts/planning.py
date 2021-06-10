#! /usr/bin/env python3

import time
import math
import rospy
import cv2 as cv
import numpy as np
from d_star_lite import DStarLite
from grid import OccupancyGridMap, SLAM

from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import Twist, Quaternion, PoseStamped

# Define some colors
BLACK = (0, 0, 0)  # BLACK
UNOCCUPIED = (255, 255, 255)  # WHITE
GOAL = (0, 255, 0)  # GREEN
START = (255, 0, 0)  # RED
ROBOT = (0, 0, 225) # BLUE
GRAY1 = (145, 145, 102)  # GRAY1
GRAY2 = (161, 161, 158)  # GRAY2
OBSTACLE = (77, 77, 51)  # GRAY2
LOCAL_GRID = (0, 0, 80)  # BLUE
TRAJ = (148, 191, 231)  # LIGHT BLUE

UNOCCUPIED = 0
TRAJ = 127
OBSTACLE = 255

n = 4

MAX_LIN_VEL = 3
MAX_ANG_VEL = 2
EPSILON = 0.05
MAX_STEP = 10000

# Global variable
p_map = np.zeros((int(2048), int(2048)), dtype=np.uint8)
g_map = np.zeros((int(512/n), int(512/n)), dtype=np.uint8) # 512, 512
flag = False

x_target = 0
y_target = 0
yaw_target = 0

def map_cb(msgs):
    global p_map, g_map, flag
    h = msgs.info.height
    w = msgs.info.width
    input = np.transpose(np.reshape(msgs.data, (h,w)))
    batch = int(4*n) # 4
    for i in range(h):
        for j in range(w):
            if input[i, j] != p_map[i, j]:
                flag = True
            if input[i, j] > 99:
                input[i, j] = OBSTACLE
            else:
                input[i, j] = UNOCCUPIED
    p_map = input
    temp = np.array(input, dtype=np.uint8)
    g_map  = temp[:(h//batch)*batch, :(w//batch)*batch].reshape(h//batch, batch, w//batch, batch).max(axis=(1, 3)).astype(int)

def quaternion_to_euler(ori):
    q0 = ori.w
    q1 = ori.x
    q2 = ori.y
    q3 = ori.z

    yaw = math.atan2(2*(q0*q3+q1*q2),1-2*(q2**2+q3**2))
    return yaw

def grid_to_real(grid_pose):
    global n

    grid_pose = np.asarray(grid_pose)

    grid_pose = grid_pose - np.round(256*np.ones((2))/n)
    real_pose = (n*grid_pose)/5
    return real_pose

def calculate_LOS(curr_pose, target, yaw):
    LOS = math.atan2((target[1]-curr_pose[1]),(target[0]-curr_pose[1]))
    return LOS

def constrain(input, low, high):
    if input < low:
      input = low
    elif input > high:
      input = high
    else:
      input = input

    return input

def checkLinearLimitVelocity(vel):
    vel = constrain(vel, -MAX_LIN_VEL, MAX_LIN_VEL)
    return vel

def checkAngularLimitVelocity(vel):
    vel = constrain(vel, -MAX_ANG_VEL, MAX_ANG_VEL)
    return vel

class Planner():
    def __init__(self, cnt, init_pose, goal):
        super(Planner, self).__init__()
        global n
        self.init_pose = tuple(init_pose.astype(int))
        self.prev_pose = tuple(init_pose.astype(int))
        self.curr_pose = tuple(init_pose.astype(int))
        self.curr_pose_real = (0,0)
        self.goal = tuple(goal.astype(int))
        self.curr_ori = Quaternion()
        self.map = OccupancyGridMap(int(512/n), int(512/n))
        self.slam = SLAM(map=self.map, view_range=int(128/n))
        self.dstar = DStarLite(map=self.map, s_start=self.init_pose, s_goal=self.goal)
        self.path = OccupancyGridMap(int(512/n), int(512/n))
        self.way = []
        self.ctrl = Twist()
        self.first = True
        self.cnt = cnt
        self.k = 0

        self.pose_sub = rospy.Subscriber("/robot"+str(cnt)+"/slam_out_pose", PoseStamped, self.pose_cb, queue_size=10)
        self.ctrl_pub = rospy.Publisher("/robot"+str(cnt)+"/cmd_vel", Twist, queue_size=10)

    def pose_cb(self, msgs):
        global n
        self.curr_pose = tuple(np.round(256*np.ones((2))/n + 5*np.array([msgs.pose.position.x, msgs.pose.position.y])/n).astype(int))
        self.curr_pose_real = (msgs.pose.position.x, msgs.pose.position.y)
        self.curr_ori = msgs.pose.orientation

    def obtain_map(self):
        global g_map
        self.map.occupancy_grid_map = g_map
        self.slam.set_ground_truth_map(gt_map = self.map)

    def planning(self):
        """
        set initial values for the map occupancy grid
        |----------> y, column
        |           (x=0,y=2)
        |
        V (x=2, y=0)
        x, row
        """
        global n, flag
        if flag:
            self.obtain_map()
            flag = False

        if self.curr_pose != self.prev_pose and not flag:
            self.prev_pose = self.curr_pose

            new_edges_and_old_costs, slam_map = self.slam.rescan(global_position=self.curr_pose)

            self.dstar.new_edges_and_old_costs = new_edges_and_old_costs
            self.dstar.sensed_map = slam_map

            # # move and compute path
            print('robot', self.cnt)
            self.way, g, rhs = self.dstar.move_and_replan(robot_position=self.curr_pose)

            # print(path)
            self.path.occupancy_grid_map = self.map.occupancy_grid_map
            for (x, y) in self.way:
                if not self.path.occupancy_grid_map[x, y]:
                    self.path.occupancy_grid_map[x, y] = TRAJ

            cv.imshow("map" + str(self.cnt), cv.resize(np.array(self.path.occupancy_grid_map, dtype=np.uint8), dsize=(0, 0), fx=n, fy=n, interpolation=cv.INTER_LINEAR))
            cv.waitKey(100)

        if self.first:
            self.first = False
            cv.imshow("map" + str(self.cnt), cv.resize(np.array(self.path.occupancy_grid_map, dtype=np.uint8), dsize=(0, 0), fx=n, fy=n, interpolation=cv.INTER_LINEAR))
            cv.waitKey(7000)

        if self.way:
            self.control(self.way[1]) # around goal ~~

    def control(self, target_pose):
        # Calculate control input to publish
        global MAX_STEP, EPSILON

        move_x = False
        move_y = False

        if target_pose[0] == self.curr_pose[0]:
            move_y = True
        elif target_pose[1] == self.curr_pose[1]:
            move_x = True

        x_curr = self.curr_pose_real[0]
        y_curr = self.curr_pose_real[1]
        yaw_curr = quaternion_to_euler(self.curr_ori) # initial: 1.57 -1.57 1.57

        target = grid_to_real(target_pose)
        x_target = target[0]
        y_target = target[1]

        LOS = calculate_LOS(self.curr_pose_real, target, yaw_curr)

        # x_error = x_target-x_curr
        # y_error = y_target-y_curr

        if move_y:
            x_error = 0
            y_error = y_target-y_curr
        elif move_x:
            x_error = x_target-x_curr
            y_error = 0

        # print(self.cnt, x_error, y_error)

        if target_pose != self.curr_pose:
            if move_y:
                x_error = 0
                y_error = y_target-y_curr
            elif move_x:
                x_error = x_target-x_curr
                y_error = 0
            # print(self.cnt, "Control in progress")
            # print(self.cnt, x_curr, y_curr, self.curr_pose[0], self.curr_pose[1], target_pose, target)
            v_x = checkLinearLimitVelocity(0.1*x_error)
            v_y = checkLinearLimitVelocity(0.1*y_error)
            self.ctrl.linear.x = v_x*math.cos(yaw_curr) + v_y*math.sin(yaw_curr) # -checkLinearLimitVelocity(0.01*x_error)
            self.ctrl.linear.y = v_y*math.cos(yaw_curr) - v_x*math.sin(yaw_curr) # -checkLinearLimitVelocity(0.01*y_error)
            self.ctrl.linear.z = 0.0

            self.ctrl.angular.x = 0.0
            self.ctrl.angular.y = 0.0
            self.ctrl.angular.z = 0

            self.ctrl_pub.publish(self.ctrl)

        elif target_pose == self.curr_pose:
            print(self.cnt, 'stop')
            self.ctrl.linear.x = 0
            self.ctrl.linear.y = 0
            self.ctrl.linear.z = 0.0

            self.ctrl.angular.x = 0.0
            self.ctrl.angular.y = 0.0
            self.ctrl.angular.z = 0.0

            self.ctrl_pub.publish(self.ctrl)

    def main(self):
        try:
            rate = rospy.Rate(0.5)
            while not rospy.is_shutdown():
                self.planning()
                rate.sleep()
            rospy.spin()

        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    try:
        rospy.init_node('planning', anonymous=False)
        map_sub = rospy.Subscriber("/map_merge/map", OccupancyGrid, map_cb, queue_size=10)
        init_pose = np.round(256*np.ones((6))/n + 5.2*np.array([-7.4, -5.5, -7.5, 15.5, 23.701897, 5.219147])/n) # 256 / -7, -5, -7, 16, 24, 6   -2, -1, -2, 4, 8, 2
        goal = np.round(256*np.ones((2))/n + 5.2*np.array([20, -4])/n) # 256 / 20, -2   5, -1
        cnt = rospy.get_param('~cnt')
        planner = Planner(cnt, init_pose[2*cnt-2:2*cnt], goal)
        planner.main()

    except rospy.ROSInterruptException:
        pass
