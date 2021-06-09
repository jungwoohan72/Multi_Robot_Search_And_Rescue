#! /usr/bin/env python3

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

# Global variable
n = 1
p_map = np.zeros((int(2048), int(2048)), dtype=np.uint8)
g_map = np.zeros((int(512/n), int(512/n)), dtype=np.uint8) # 512, 512
flag = False

def map_cb(msgs):
    global p_map, g_map, flag
    h = msgs.info.height
    w = msgs.info.width
    input = np.transpose(np.reshape(msgs.data, (h,w)))
    batch = int(4*n) # 4
    flag = False
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

class Planner():
    def __init__(self, cnt, init_pose, goal):
        super(Planner, self).__init__()
        global n
        self.init_pose = tuple(init_pose.astype(int))
        self.prev_pose = tuple(init_pose.astype(int))
        self.curr_pose = tuple(init_pose.astype(int))
        self.goal = tuple(goal.astype(int))
        self.curr_ori = Quaternion()
        self.map = OccupancyGridMap(int(512/n), int(512/n))
        self.slam = SLAM(map=self.map, view_range=int(5*4/n))
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

        if self.curr_pose != self.prev_pose or self.first:
            self.prev_pose = self.curr_pose

            new_edges_and_old_costs, slam_map = self.slam.rescan(global_position=self.curr_pose)

            self.dstar.new_edges_and_old_costs = new_edges_and_old_costs
            self.dstar.sensed_map = slam_map

            # # move and compute path
            self.way, g, rhs = self.dstar.move_and_replan(robot_position=self.curr_pose)
            self.first = False

        # print(path)
        self.path.occupancy_grid_map = self.map.occupancy_grid_map
        for (x, y) in self.way:
            if not self.path.occupancy_grid_map[x, y]:
                self.path.occupancy_grid_map[x, y] = TRAJ

        cv.imshow("map" + str(self.cnt), np.array(self.path.occupancy_grid_map, dtype=np.uint8))

        key = cv.waitKey(1000)

        self.control()

    def control(self):
        # Calculate control input to publish
        self.ctrl.linear.x = 0.0
        self.ctrl.linear.y = 0.0
        self.ctrl.linear.z = 0.0

        self.ctrl.angular.x = 0.0
        self.ctrl.angular.y = 0.0
        self.ctrl.angular.z = 0.0

        self.ctrl_pub.publish(self.ctrl)
        print("publish"+str(self.cnt))

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
        init_pose = np.round(256*np.ones((6))/n + 5*np.array([-7.4, -5.5, -7.5, 15.5, 23.701897, 5.219147])/n) # 256 / -7, -5, -7, 16, 24, 6   -2, -1, -2, 4, 8, 2
        goal = np.round(256*np.ones((2))/n + 5*np.array([20, -4])/n) # 256 / 20, -2   5, -1
        cnt = rospy.get_param('~cnt')
        planner = Planner(cnt, init_pose[2*cnt-2:2*cnt], goal)
        planner.main()

    except rospy.ROSInterruptException:
        pass