#! /usr/bin/env python3

import rospy
import cv2 as cv
import numpy as np
from d_star_lite import DStarLite
from grid import OccupancyGridMap, SLAM

from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import Twist

import multiprocessing

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
TRAJ = 2
OBSTACLE = 255

# Global variable
k = 0; h = 512; w = 512
start = np.zeros(2)
goal = np.zeros(2)
current = np.zeros(2)
g_map = np.zeros((h,w))

class Planner(multiprocessing.Process):
    def __init__(self, i):
        super(Planner, self).__init__()
        global h, w
        self.map_sub = rospy.Subscriber("/robot"+str(i)+"/map", OccupancyGrid, self.map_cb, queue_size=1)
        self.ctrl_pub = rospy.Publisher("/robot"+str(i)+"/cmd_vel", Twist, queue_size=10)
        self.map = np.zeros((h,w))
        self.cnt = i
        
    def map_cb(self, msgs):
        global k
        h = msgs.info.height
        w = msgs.info.width
        input = np.transpose(np.reshape(msgs.data, (h,w)))
        batch = 4
        for i in range(h):
            for j in range(w):
                if input[i, j] == 100:
                    input[i, j] = 255
                else:
                    input[i, j] = 0
        temp = np.array(input, dtype=np.uint8)
        map = temp[:(h//batch)*batch, :(w//batch)*batch].reshape(h//batch, batch, w//batch, batch).max(axis=(1, 3))
        self.map = map
        self.local2world()
    
    def local2world(self):
        # transform local map to world map
        global g_map, k, h, w
        for i in range(h):
            for j in range(w):
                if not g_map[i, j] and self.map[i, j]:
                    g_map[i, j] += self.map[i, j]

    def planning(self):
        """
        set initial values for the map occupancy grid
        |----------> y, column
        |           (x=0,y=2)
        |
        V (x=2, y=0)
        x, row
        """
        global start, goal, current, k, h, w, g_map

        # gui = Animation(title="D* Lite Path Planning",
        #                 width=10,
        #                 height=10,
        #                 margin=0,
        #                 x_dim=h,
        #                 y_dim=w,
        #                 start=start,
        #                 goal=goal)

        # D* Lite (optimized)
        # dstar = DStarLite(map=self.map,
        #                 s_start=start,
        #                 s_goal=goal)

        # # move and compute path
        # path, g, rhs = dstar.move_and_replan(robot_position=current)

        # gui.run_game(path=path)
        k += 1
        if k%10 == 0:
            cv.imshow('map'+str(self.cnt)+'-'+str(k), self.map)
            cv.imshow('map'+str(k), g_map)

        self.control()

    def control(self):
        # Calculate control input to publish
        # ctrl = Twist()

        # ctrl.linear.x = 0.5
        # ctrl.linear.y = 0.0
        # ctrl.linear.z = 0.0

        # ctrl.angular.x = 0.0
        # ctrl.angular.y = 0.0
        # ctrl.angular.z = 0.0

        # print("publish"+str(self.cnt))
        # self.ctrl_pub.publish(ctrl)
        pass

    def main(self):
        try:
            rate = rospy.Rate(5)
            self.planning()
            rate.sleep()

        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    try:
        rospy.init_node('planning', anonymous=False)
        for i in range(1, 4):
            globals()['p{}'.format(i)] = Planner(i)
        while not rospy.is_shutdown():
            for i in range(1, 4):
                globals()['p{}'.format(i)].main()

        rospy.spin()

    except rospy.ROSInterruptException:
        pass