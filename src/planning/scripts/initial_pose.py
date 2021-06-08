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
from sensor_msgs.msg import LaserScan

class InitialPoseGenerator:
    def __init__(self):
        rospy.init_node('initial_pose_generator')
        self.pub0 = rospy.Publisher('/robot1/initialpose', PoseWithCovarianceStamped, queue_size=100)
        self.pub1 = rospy.Publisher('/robot1/initialpose', PoseWithCovarianceStamped, queue_size=100)
        self.pub2 = rospy.Publisher('/robot2/initialpose', PoseWithCovarianceStamped, queue_size=100)
        self.pub3 = rospy.Publisher('/robot3/initialpose', PoseWithCovarianceStamped, queue_size=100)

        # self.pub11 = rospy.Publisher('/robot1/scan', LaserScan, queue_size=100)
        # self.pub21 = rospy.Publisher('/robot2/scan', LaserScan, queue_size=100)
        # self.pub31 = rospy.Publisher('/robot3/scan', LaserScan, queue_size=100)

        self.rate = rospy.Rate(1)

    def initial_pose_publish(self):
        # robot1_scan = LaserScan()
        # robot2_scan = LaserScan()
        # robot3_scan = LaserScan()

        # robot1_scan.header.frame_id = "robot1/Lidar"
        # robot1_scan.header.seq = 0
        # robot1_scan.header.stamp.secs = 22
        # robot1_scan.header.stamp.nsecs = 604000000
        # robot1_scan.angle_min = -3.1400001049
        # robot1_scan.angle_max = 3.1400001049
        # robot1_scan.angle_increment = 0.0174930356443
        # robot1_scan.time_increment = 0.0
        # robot1_scan.scan_time = 0.0
        # robot1_scan.range_min = 0.00999999977648
        # robot1_scan.range_max = 4.0
        
        # robot2_scan.header.frame_id = "robot2/Lidar"
        # robot2_scan.header.seq = 0
        # robot2_scan.header.stamp.secs = 22
        # robot2_scan.header.stamp.nsecs = 604000000
        # robot2_scan.angle_min = -3.1400001049
        # robot2_scan.angle_max = 3.1400001049
        # robot2_scan.angle_increment = 0.0174930356443
        # robot2_scan.time_increment = 0.0
        # robot2_scan.scan_time = 0.0
        # robot2_scan.range_min = 0.00999999977648
        # robot2_scan.range_max = 4.0

        # robot3_scan.header.frame_id = "robot3/Lidar"
        # robot3_scan.header.seq = 0
        # robot3_scan.header.stamp.secs = 22
        # robot3_scan.header.stamp.nsecs = 604000000
        # robot3_scan.angle_min = -3.1400001049
        # robot3_scan.angle_max = 3.1400001049
        # robot3_scan.angle_increment = 0.0174930356443
        # robot3_scan.time_increment = 0.0
        # robot3_scan.scan_time = 0.0
        # robot3_scan.range_min = 0.00999999977648
        # robot3_scan.range_max = 4.0

        # self.pub11.publish(robot1_scan)
        # self.pub21.publish(robot2_scan)
        # self.pub31.publish(robot3_scan)

        robot0_initial = PoseWithCovarianceStamped()
        robot1_initial = PoseWithCovarianceStamped()
        robot2_initial = PoseWithCovarianceStamped()
        robot3_initial = PoseWithCovarianceStamped()

        robot0_initial.header.frame_id = "robot0/Lidar"
        robot0_initial.pose.pose.position.x = 0
        robot0_initial.pose.pose.position.y = 0
        robot0_initial.pose.pose.position.z = 0
        robot0_initial.pose.pose.orientation.w = 1
        robot0_initial.pose.pose.orientation.x = 0
        robot0_initial.pose.pose.orientation.y = 0
        robot0_initial.pose.pose.orientation.z = 0

        robot1_initial.header.frame_id = "robot1/base_link"
        robot1_initial.pose.pose.position.x = -7.4
        robot1_initial.pose.pose.position.y = -5.5
        robot1_initial.pose.pose.position.z = 0
        robot1_initial.pose.pose.orientation.w = 0.707
        robot1_initial.pose.pose.orientation.x = 0
        robot1_initial.pose.pose.orientation.y = 0
        robot1_initial.pose.pose.orientation.z = 0.707

        robot2_initial.header.frame_id = "robot2/base_link"
        robot2_initial.pose.pose.position.x = -7.5
        robot2_initial.pose.pose.position.y = 15.5
        robot2_initial.pose.pose.position.z = 0
        robot2_initial.pose.pose.orientation.w = 0.707
        robot2_initial.pose.pose.orientation.x = 0
        robot2_initial.pose.pose.orientation.y = 0
        robot2_initial.pose.pose.orientation.z = -0.707

        robot3_initial.header.frame_id = "robot3/base_link"
        robot3_initial.pose.pose.position.x = 23.701897
        robot3_initial.pose.pose.position.y = 5.219147
        robot3_initial.pose.pose.position.z = 0
        robot3_initial.pose.pose.orientation.w = 0.707
        robot3_initial.pose.pose.orientation.x = 0
        robot3_initial.pose.pose.orientation.y = 0
        robot3_initial.pose.pose.orientation.z = 0.707

        self.pub0.publish(robot0_initial)
        self.pub1.publish(robot1_initial)
        self.pub2.publish(robot2_initial)
        self.pub3.publish(robot3_initial)

if __name__ == '__main__':
    initial_pose_generator = InitialPoseGenerator()

    while not rospy.is_shutdown():
        initial_pose_generator.initial_pose_publish()
        initial_pose_generator.rate.sleep()
        print("Running")
