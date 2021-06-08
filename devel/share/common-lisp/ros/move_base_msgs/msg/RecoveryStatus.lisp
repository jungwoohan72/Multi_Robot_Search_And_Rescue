; Auto-generated. Do not edit!


(cl:in-package move_base_msgs-msg)


;//! \htmlinclude RecoveryStatus.msg.html

(cl:defclass <RecoveryStatus> (roslisp-msg-protocol:ros-message)
  ((pose_stamped
    :reader pose_stamped
    :initarg :pose_stamped
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (current_recovery_number
    :reader current_recovery_number
    :initarg :current_recovery_number
    :type cl:fixnum
    :initform 0)
   (total_number_of_recoveries
    :reader total_number_of_recoveries
    :initarg :total_number_of_recoveries
    :type cl:fixnum
    :initform 0)
   (recovery_behavior_name
    :reader recovery_behavior_name
    :initarg :recovery_behavior_name
    :type cl:string
    :initform ""))
)

(cl:defclass RecoveryStatus (<RecoveryStatus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RecoveryStatus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RecoveryStatus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name move_base_msgs-msg:<RecoveryStatus> is deprecated: use move_base_msgs-msg:RecoveryStatus instead.")))

(cl:ensure-generic-function 'pose_stamped-val :lambda-list '(m))
(cl:defmethod pose_stamped-val ((m <RecoveryStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader move_base_msgs-msg:pose_stamped-val is deprecated.  Use move_base_msgs-msg:pose_stamped instead.")
  (pose_stamped m))

(cl:ensure-generic-function 'current_recovery_number-val :lambda-list '(m))
(cl:defmethod current_recovery_number-val ((m <RecoveryStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader move_base_msgs-msg:current_recovery_number-val is deprecated.  Use move_base_msgs-msg:current_recovery_number instead.")
  (current_recovery_number m))

(cl:ensure-generic-function 'total_number_of_recoveries-val :lambda-list '(m))
(cl:defmethod total_number_of_recoveries-val ((m <RecoveryStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader move_base_msgs-msg:total_number_of_recoveries-val is deprecated.  Use move_base_msgs-msg:total_number_of_recoveries instead.")
  (total_number_of_recoveries m))

(cl:ensure-generic-function 'recovery_behavior_name-val :lambda-list '(m))
(cl:defmethod recovery_behavior_name-val ((m <RecoveryStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader move_base_msgs-msg:recovery_behavior_name-val is deprecated.  Use move_base_msgs-msg:recovery_behavior_name instead.")
  (recovery_behavior_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RecoveryStatus>) ostream)
  "Serializes a message object of type '<RecoveryStatus>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose_stamped) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'current_recovery_number)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'current_recovery_number)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'total_number_of_recoveries)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'total_number_of_recoveries)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'recovery_behavior_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'recovery_behavior_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RecoveryStatus>) istream)
  "Deserializes a message object of type '<RecoveryStatus>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose_stamped) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'current_recovery_number)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'current_recovery_number)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'total_number_of_recoveries)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'total_number_of_recoveries)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'recovery_behavior_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'recovery_behavior_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RecoveryStatus>)))
  "Returns string type for a message object of type '<RecoveryStatus>"
  "move_base_msgs/RecoveryStatus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecoveryStatus)))
  "Returns string type for a message object of type 'RecoveryStatus"
  "move_base_msgs/RecoveryStatus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RecoveryStatus>)))
  "Returns md5sum for a message object of type '<RecoveryStatus>"
  "a2488e0805e1529a31044786ee1a2623")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RecoveryStatus)))
  "Returns md5sum for a message object of type 'RecoveryStatus"
  "a2488e0805e1529a31044786ee1a2623")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RecoveryStatus>)))
  "Returns full string definition for message of type '<RecoveryStatus>"
  (cl:format cl:nil "geometry_msgs/PoseStamped pose_stamped  # The robot's pose when the recovery was triggered~%uint16 current_recovery_number          # 0-based index of current recovery number~%uint16 total_number_of_recoveries       # Total number of recoveries configured~%string recovery_behavior_name           # Namespace of the recovery being executed~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RecoveryStatus)))
  "Returns full string definition for message of type 'RecoveryStatus"
  (cl:format cl:nil "geometry_msgs/PoseStamped pose_stamped  # The robot's pose when the recovery was triggered~%uint16 current_recovery_number          # 0-based index of current recovery number~%uint16 total_number_of_recoveries       # Total number of recoveries configured~%string recovery_behavior_name           # Namespace of the recovery being executed~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RecoveryStatus>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose_stamped))
     2
     2
     4 (cl:length (cl:slot-value msg 'recovery_behavior_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RecoveryStatus>))
  "Converts a ROS message object to a list"
  (cl:list 'RecoveryStatus
    (cl:cons ':pose_stamped (pose_stamped msg))
    (cl:cons ':current_recovery_number (current_recovery_number msg))
    (cl:cons ':total_number_of_recoveries (total_number_of_recoveries msg))
    (cl:cons ':recovery_behavior_name (recovery_behavior_name msg))
))
