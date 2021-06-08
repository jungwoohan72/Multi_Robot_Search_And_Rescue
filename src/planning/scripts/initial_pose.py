import rospy
import rospkg
import roslib
import pdb
import math

from gazebo_msgs.msg import ModelStates
from gazebo_msgs.msg import ModelState
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseWithCovarianceStamped

class InitialPoseGenerator:
    def __init__(self):
        rospy.init_node('initial_pose_generator')
        self.pub1 = rospy.Publisher('/robot1/initialpose', PoseWithCovarianceStamped, queue_size=100)
        self.pub2 = rospy.Publisher('/robot2/initialpose', PoseWithCovarianceStamped, queue_size=100)
        self.pub3 = rospy.Publisher('/robot3/initialpose', PoseWithCovarianceStamped, queue_size=100)

        self.rate = rospy.Rate(1)

    def initial_pose_publish(self):
        robot1_initial = PoseWithCovarianceStamped()
        robot2_initial = PoseWithCovarianceStamped()
        robot3_initial = PoseWithCovarianceStamped()

        robot1_initial.header.frame_id = "robot1/Lidar"
        robot1_initial.pose.pose.position.x = -7.4
        robot1_initial.pose.pose.position.y = -5.5
        robot1_initial.pose.pose.position.z = 0
        robot1_initial.pose.pose.orientation.w = 0.707
        robot1_initial.pose.pose.orientation.x = 0
        robot1_initial.pose.pose.orientation.y = 0
        robot1_initial.pose.pose.orientation.z = 0.707

        robot2_initial.header.frame_id = "robot2/Lidar"
        robot2_initial.pose.pose.position.x = -7.5
        robot2_initial.pose.pose.position.y = 15.5
        robot2_initial.pose.pose.position.z = 0
        robot2_initial.pose.pose.orientation.w = 0.707
        robot2_initial.pose.pose.orientation.x = 0
        robot2_initial.pose.pose.orientation.y = 0
        robot2_initial.pose.pose.orientation.z = -0.707

        robot3_initial.header.frame_id = "robot3/Lidar"
        robot3_initial.pose.pose.position.x = 35
        robot3_initial.pose.pose.position.y = 9
        robot3_initial.pose.pose.position.z = 0
        robot3_initial.pose.pose.orientation.w = 0
        robot3_initial.pose.pose.orientation.x = 0
        robot3_initial.pose.pose.orientation.y = 0
        robot3_initial.pose.pose.orientation.z = 1

        self.pub1.publish(robot1_initial)
        self.pub2.publish(robot2_initial)
        self.pub3.publish(robot3_initial)

if __name__ == '__main__':
    initial_pose_generator = InitialPoseGenerator()

    while not rospy.is_shutdown():
        initial_pose_generator.initial_pose_publish()
        initial_pose_generator.rate.sleep()
        print("Running")
