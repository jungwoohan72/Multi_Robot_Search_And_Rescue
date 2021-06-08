// Auto-generated. Do not edit!

// (in-package move_base_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class RecoveryStatus {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pose_stamped = null;
      this.current_recovery_number = null;
      this.total_number_of_recoveries = null;
      this.recovery_behavior_name = null;
    }
    else {
      if (initObj.hasOwnProperty('pose_stamped')) {
        this.pose_stamped = initObj.pose_stamped
      }
      else {
        this.pose_stamped = new geometry_msgs.msg.PoseStamped();
      }
      if (initObj.hasOwnProperty('current_recovery_number')) {
        this.current_recovery_number = initObj.current_recovery_number
      }
      else {
        this.current_recovery_number = 0;
      }
      if (initObj.hasOwnProperty('total_number_of_recoveries')) {
        this.total_number_of_recoveries = initObj.total_number_of_recoveries
      }
      else {
        this.total_number_of_recoveries = 0;
      }
      if (initObj.hasOwnProperty('recovery_behavior_name')) {
        this.recovery_behavior_name = initObj.recovery_behavior_name
      }
      else {
        this.recovery_behavior_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RecoveryStatus
    // Serialize message field [pose_stamped]
    bufferOffset = geometry_msgs.msg.PoseStamped.serialize(obj.pose_stamped, buffer, bufferOffset);
    // Serialize message field [current_recovery_number]
    bufferOffset = _serializer.uint16(obj.current_recovery_number, buffer, bufferOffset);
    // Serialize message field [total_number_of_recoveries]
    bufferOffset = _serializer.uint16(obj.total_number_of_recoveries, buffer, bufferOffset);
    // Serialize message field [recovery_behavior_name]
    bufferOffset = _serializer.string(obj.recovery_behavior_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RecoveryStatus
    let len;
    let data = new RecoveryStatus(null);
    // Deserialize message field [pose_stamped]
    data.pose_stamped = geometry_msgs.msg.PoseStamped.deserialize(buffer, bufferOffset);
    // Deserialize message field [current_recovery_number]
    data.current_recovery_number = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [total_number_of_recoveries]
    data.total_number_of_recoveries = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [recovery_behavior_name]
    data.recovery_behavior_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += geometry_msgs.msg.PoseStamped.getMessageSize(object.pose_stamped);
    length += object.recovery_behavior_name.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'move_base_msgs/RecoveryStatus';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a2488e0805e1529a31044786ee1a2623';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/PoseStamped pose_stamped  # The robot's pose when the recovery was triggered
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RecoveryStatus(null);
    if (msg.pose_stamped !== undefined) {
      resolved.pose_stamped = geometry_msgs.msg.PoseStamped.Resolve(msg.pose_stamped)
    }
    else {
      resolved.pose_stamped = new geometry_msgs.msg.PoseStamped()
    }

    if (msg.current_recovery_number !== undefined) {
      resolved.current_recovery_number = msg.current_recovery_number;
    }
    else {
      resolved.current_recovery_number = 0
    }

    if (msg.total_number_of_recoveries !== undefined) {
      resolved.total_number_of_recoveries = msg.total_number_of_recoveries;
    }
    else {
      resolved.total_number_of_recoveries = 0
    }

    if (msg.recovery_behavior_name !== undefined) {
      resolved.recovery_behavior_name = msg.recovery_behavior_name;
    }
    else {
      resolved.recovery_behavior_name = ''
    }

    return resolved;
    }
};

module.exports = RecoveryStatus;
