#! /usr/bin/env python3

import rospy
import cv2 as cv
import numpy as np
from grid import OccupancyGridMap

from std_msgs.msg import Float64MultiArray
from nav_msgs.msg import OccupancyGrid

k = 0

class planner(object):
    def __init__(self):
        self.map_sub = rospy.Subscriber("/map", OccupancyGrid, self.map_cb, queue_size=1)
        self.pl_pub = rospy.Publisher("/cmd", Float64MultiArray,queue_size=1)
        self.map_input = np.array([])
        
    def map_cb(self, msgs):
        global k
        h = msgs.info.height
        w = msgs.info.width
        input = np.transpose(np.reshape(msgs.data, (h,w)))
        batch = 5
        for i in range(h):
            for j in range(w):
                if input[i, j] == 100:
                    input[i, j] = 255
                else:
                    input[i, j] = 0
        temp = np.array(input, dtype=np.uint8)
        map = temp[:(h//batch)*batch, :(w//batch)*batch].reshape(h//batch, batch, w//batch, batch).max(axis=(1, 3))
        self.map_input = map
        path = '/home/morin-sol/ME652/output/map'+str(k)+'.jpg'
        cv.imwrite(path, map)
        print(path)
        k += 1
    
    def planning(self):
        rate = rospy.Rate(5)
        rate.sleep()

    def main(self):
        try:
            rate = rospy.Rate(5)
            while not rospy.is_shutdown():
                self.planning()
                rate.sleep()

        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    try:
        rospy.init_node('planning', anonymous=False)
        p = planner()
        p.main()

        rospy.spin()

    except rospy.ROSInterruptException:
        pass

# from d_star_lite import DStarLite
# from grid import OccupancyGridMap, SLAM

# # Define some colors
# BLACK = (0, 0, 0)  # BLACK
# UNOCCUPIED = (255, 255, 255)  # WHITE
# GOAL = (0, 255, 0)  # GREEN
# START = (255, 0, 0)  # RED
# ROBOT = (0, 0, 225) # BLUE
# GRAY1 = (145, 145, 102)  # GRAY1
# GRAY2 = (161, 161, 158)  # GRAY2
# OBSTACLE = (77, 77, 51)  # GRAY2
# LOCAL_GRID = (0, 0, 80)  # BLUE
# TRAJ = (148, 191, 231)  # LIGHT BLUE

# UNOCCUPIED = 0
# TRAJ = 2
# OBSTACLE = 255

# if __name__ == '__main__':

#     """
#     set initial values for the map occupancy grid
#     |----------> y, column
#     |           (x=0,y=2)
#     |
#     V (x=2, y=0)
#     x, row
#     """
#     x_dim = 102
#     y_dim = 102
#     start = (1, 1)
#     goal = (82, 85)
#     view_range = 5

#     gui = Animation(title="D* Lite Path Planning",
#                     width=10,
#                     height=10,
#                     margin=0,
#                     x_dim=x_dim,
#                     y_dim=y_dim,
#                     start=start,
#                     goal=goal,
#                     viewing_range=view_range,
#                     slam = False)

#     gui_SLAM = Animation(title="D* Lite Path Planning",
#                     width=10,
#                     height=10,
#                     margin=0,
#                     x_dim=x_dim,
#                     y_dim=y_dim,
#                     start=start,
#                     goal=goal,
#                     viewing_range=view_range,
#                     slam = True)

#     # Environment Setting
#     static_obstacle_map = EnvironmentSetting(gui)
#     # static_obstacle_map.block(10,10,4)
#     static_obstacle_map.warehouse_environment1()

#     # Dynamic Obstacle initialization
#     obstacle_1 = DynamicObstacle(gui=gui, x=5, y=5, is_horizontal = True, start=(18,25), end=(18,10), v = 5, reverse = True)
#     obstacle_2 = DynamicObstacle(gui=gui, x=6, y=6, is_horizontal = False, start=(80,77), end=(40,77), v = 15, reverse = True)
#     obstacle_3 = DynamicObstacle(gui=gui, x=10, y=10, is_horizontal = False, start=(40,50), end=(80,50), v = 10, reverse = False)
#     obstacle_4 = DynamicObstacle(gui=gui, x=5, y=5, is_horizontal = True, start=(60,65), end=(60,42), v = 5, reverse = True)
#     obstacle_5 = DynamicObstacle(gui=gui, x=8, y=8, is_horizontal = False, start=(30,30), end=(10,30), v = 5, reverse = True)

#     new_map = gui.world
#     old_map = new_map

#     new_position = start
#     last_position = start

#     # new_observation = None
#     # type = OBSTACLE

#     # D* Lite (optimized)
#     dstar = DStarLite(map=new_map,
#                       s_start=start,
#                       s_goal=goal)

#     # SLAM to detect vertices
#     slam = SLAM(map=new_map,
#                 view_range=view_range)

#     # move and compute path
#     path, g, rhs = dstar.move_and_replan(robot_position=new_position)

#     while not gui.done:
#         # update the map
#         # print(path)
#         # drive gui
#         gui.run_game(path=path)

#         new_position = gui.current
#         new_observation = gui.observation
#         new_map = gui.world

#         """
#         if new_observation is not None:
#             if new_observation["type"] == OBSTACLE:
#                 dstar.global_map.set_obstacle(pos=new_observation["pos"])
#             if new_observation["pos"] == UNOCCUPIED:
#                 dstar.global_map.remove_obstacle(pos=new_observation["pos"])
#         """

#         if new_observation is not None:
#             old_map = new_map
#             slam.set_ground_truth_map(gt_map=new_map)

#         if new_position != last_position:
#             last_position = new_position
#             obstacle_1.move()
#             obstacle_2.move()
#             obstacle_3.move()
#             obstacle_4.move()
#             obstacle_5.move()

#             # slam
#             new_edges_and_old_costs, slam_map = slam.rescan(global_position=new_position)

#             dstar.new_edges_and_old_costs = new_edges_and_old_costs
#             dstar.sensed_map = slam_map

#             # d star
#             path, g, rhs = dstar.move_and_replan(robot_position=new_position)

#         if gui.world.occupancy_grid_map[start[0]][start[1]] == UNOCCUPIED:
#             gui.world.occupancy_grid_map[start[0]][start[1]] = TRAJ
#         gui.world.occupancy_grid_map[new_position[0]][new_position[1]] = TRAJ
        
#         gui_SLAM.run_game(path=path, world=dstar.sensed_map)

#         if gui_SLAM.world.occupancy_grid_map[start[0]][start[1]] == UNOCCUPIED:
#             gui_SLAM.world.occupancy_grid_map[start[0]][start[1]] = TRAJ
#         gui_SLAM.world.occupancy_grid_map[new_position[0]][new_position[1]] = TRAJ