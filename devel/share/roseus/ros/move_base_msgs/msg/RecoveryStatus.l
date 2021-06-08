;; Auto-generated. Do not edit!


(when (boundp 'move_base_msgs::RecoveryStatus)
  (if (not (find-package "MOVE_BASE_MSGS"))
    (make-package "MOVE_BASE_MSGS"))
  (shadow 'RecoveryStatus (find-package "MOVE_BASE_MSGS")))
(unless (find-package "MOVE_BASE_MSGS::RECOVERYSTATUS")
  (make-package "MOVE_BASE_MSGS::RECOVERYSTATUS"))

(in-package "ROS")
;;//! \htmlinclude RecoveryStatus.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass move_base_msgs::RecoveryStatus
  :super ros::object
  :slots (_pose_stamped _current_recovery_number _total_number_of_recoveries _recovery_behavior_name ))

(defmethod move_base_msgs::RecoveryStatus
  (:init
   (&key
    ((:pose_stamped __pose_stamped) (instance geometry_msgs::PoseStamped :init))
    ((:current_recovery_number __current_recovery_number) 0)
    ((:total_number_of_recoveries __total_number_of_recoveries) 0)
    ((:recovery_behavior_name __recovery_behavior_name) "")
    )
   (send-super :init)
   (setq _pose_stamped __pose_stamped)
   (setq _current_recovery_number (round __current_recovery_number))
   (setq _total_number_of_recoveries (round __total_number_of_recoveries))
   (setq _recovery_behavior_name (string __recovery_behavior_name))
   self)
  (:pose_stamped
   (&rest __pose_stamped)
   (if (keywordp (car __pose_stamped))
       (send* _pose_stamped __pose_stamped)
     (progn
       (if __pose_stamped (setq _pose_stamped (car __pose_stamped)))
       _pose_stamped)))
  (:current_recovery_number
   (&optional __current_recovery_number)
   (if __current_recovery_number (setq _current_recovery_number __current_recovery_number)) _current_recovery_number)
  (:total_number_of_recoveries
   (&optional __total_number_of_recoveries)
   (if __total_number_of_recoveries (setq _total_number_of_recoveries __total_number_of_recoveries)) _total_number_of_recoveries)
  (:recovery_behavior_name
   (&optional __recovery_behavior_name)
   (if __recovery_behavior_name (setq _recovery_behavior_name __recovery_behavior_name)) _recovery_behavior_name)
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/PoseStamped _pose_stamped
    (send _pose_stamped :serialization-length)
    ;; uint16 _current_recovery_number
    2
    ;; uint16 _total_number_of_recoveries
    2
    ;; string _recovery_behavior_name
    4 (length _recovery_behavior_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/PoseStamped _pose_stamped
       (send _pose_stamped :serialize s)
     ;; uint16 _current_recovery_number
       (write-word _current_recovery_number s)
     ;; uint16 _total_number_of_recoveries
       (write-word _total_number_of_recoveries s)
     ;; string _recovery_behavior_name
       (write-long (length _recovery_behavior_name) s) (princ _recovery_behavior_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/PoseStamped _pose_stamped
     (send _pose_stamped :deserialize buf ptr-) (incf ptr- (send _pose_stamped :serialization-length))
   ;; uint16 _current_recovery_number
     (setq _current_recovery_number (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _total_number_of_recoveries
     (setq _total_number_of_recoveries (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; string _recovery_behavior_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _recovery_behavior_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get move_base_msgs::RecoveryStatus :md5sum-) "a2488e0805e1529a31044786ee1a2623")
(setf (get move_base_msgs::RecoveryStatus :datatype-) "move_base_msgs/RecoveryStatus")
(setf (get move_base_msgs::RecoveryStatus :definition-)
      "geometry_msgs/PoseStamped pose_stamped  # The robot's pose when the recovery was triggered
uint16 current_recovery_number          # 0-based index of current recovery number
uint16 total_number_of_recoveries       # Total number of recoveries configured
string recovery_behavior_name           # Namespace of the recovery being executed

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :move_base_msgs/RecoveryStatus "a2488e0805e1529a31044786ee1a2623")


