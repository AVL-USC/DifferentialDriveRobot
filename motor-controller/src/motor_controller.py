#!/usr/bin/env python
from roboclaw import Roboclaw
import time
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float32 
import numpy as np

roboclaw = Roboclaw("/dev/ttyACM0", 115200)
roboclaw.Open()
address = 0x80
roboclaw.ResetEncoders(address)

def set_l_motor_velocity(data):
    rospy.loginfo(data)
    data = np.clip(data, -10,10)
    if data < 0:
        roboclaw.BackwardM1(address, data)
    else:
        roboclaw.ForwardM1(address, data)

def set_r_motor_velocity(data):
    rospy.loginfo(data)
    data = np.clip(data, -10,10)
    if data < 0:
        roboclaw.BackwardM2(address, data)
    else:
        roboclaw.ForwardM2(address, data)

def motor():
    #init motor controller ros node
    l_encoder = rospy.Publisher('lwheel', Int16, queue_size=10)
    r_encoder = rospy.Publisher('rwheel', Int16, queue_size=10)
    rospy.Subscriber('lmotor_cmd', Float32, set_l_motor_velocity)
    rospy.Subscriber('rmotor_cmd', Float32, set_l_motor_velocity)
    rospy.init_node('motorController', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #init roboclaw motor controller
    while not rospy.is_shutdown():
        right_encoder_value = roboclaw.ReadEncM1(address)
        left_encoder_value = roboclaw.ReadEncM2(address)
        rospy.loginfo(right_encoder_value)
        rospy.loginfo(left_encoder_value)
        r_encoder.publish(right_encoder_value[1])
        l_encoder.publish(left_encoder_value[1])
        rate.sleep()


if __name__ == '__main__':
    try:
        motor()
    except rospy.ROSInterruptException:
        pass


