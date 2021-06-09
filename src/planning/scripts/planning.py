#! /usr/bin/env python3

import rospy
import numpy as np
from d_star_lite import DStarLite
from grid import OccupancyGridMap

from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import Twist, Quaternion, PoseStamped

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
g_map = np.zeros((512, 512), dtype=np.uint8)

def map_cb(msgs):
    global g_map
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
    g_map  = temp[:(h//batch)*batch, :(w//batch)*batch].reshape(h//batch, batch, w//batch, batch).max(axis=(1, 3)).astype(int)

class Planner(multiprocessing.Process):
    def __init__(self, i, init_pose, goal):
        super(Planner, self).__init__()
        self.init_pose = tuple(init_pose.astype(int))
        self.curr_pose = tuple(np.zeros((2)).astype(int))
        self.goal = tuple(goal.astype(int))
        self.curr_ori = Quaternion()
        self.pose_sub = rospy.Subscriber("/robot"+str(i)+"/slam_out_pose", PoseStamped, queue_size=10)
        self.ctrl_pub = rospy.Publisher("/robot"+str(i)+"/cmd_vel", Twist, queue_size=10)
        self.map = OccupancyGridMap(512, 512)
        self.cnt = i

    def pose_cb(self, msgs):
        self.curr_pose = np.array([msgs.pose.position.x, msgs.pose.position.y]).astype(int)
        self.curr_ori = msgs.pose.orientation
        # pose trans

    def obtain_map(self):
        global g_map
        self.map.occupancy_grid_map = g_map

    def planning(self):
        """
        set initial values for the map occupancy grid
        |----------> y, column
        |           (x=0,y=2)
        |
        V (x=2, y=0)
        x, row
        """
        self.obtain_map()

        # D* Lite (optimized)
        dstar = DStarLite(map=self.map, s_start=self.init_pose, s_goal=self.goal)

        # # move and compute path
        path, g, rhs = dstar.move_and_replan(robot_position=self.curr_pose)

        self.control()

    def control(self):
        # Calculate control input to publish
        ctrl = Twist()

        ctrl.linear.x = 0.5
        ctrl.linear.y = 0.0
        ctrl.linear.z = 0.0

        ctrl.angular.x = 0.0
        ctrl.angular.y = 0.0
        ctrl.angular.z = 0.0

        self.ctrl_pub.publish(ctrl)
        print("publish"+str(self.cnt))

    def run(self):
        try:
            rate = rospy.Rate(1)
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
        init_pose = 256*np.ones((6)) + np.array([-7, -5, -7, 16, 24, 6])
        goal = 256*np.ones((2)) + np.array([20, -2])
        for i in range(1, 4):
            globals()['p{}'.format(i)] = Planner(i, init_pose[2*i-2:2*i], goal)
            globals()['p{}'.format(i)].start()

    except rospy.ROSInterruptException:
        pass