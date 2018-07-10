#!/usr/bin/env python

import rospy
from first_smach.msg import State

rospy.init_node('dummy_pub')
pub = rospy.Publisher('state', State, queue_size=10)

loop_rate = rospy.Rate(1)

while not rospy.is_shutdown():
    msg = State()
    msg.statename = 'Hoge'
    msg.id = 'HogeHoge'
    msg.src = ['success', 'failed']
    msg.dst = ['Fooooo', 'HogeHoge']
    msg.is_end = False
    pub.publish(msg)
    msg = State()
    msg.statename = 'Foo'
    msg.id = 'Fooooo'
    msg.src = ['success', 'failed']
    msg.dst = ['success', 'Recovery']
    msg.is_end = False
    pub.publish(msg)
    msg = State()
    msg.statename = 'Recovery'
    msg.id = 'Recovery'
    msg.src = ['success', 'failed']
    msg.dst = ['HogeHoge', 'failed']
    msg.keywords = ['sleeptime']
    msg.args = ['3']
    msg.is_end = True
    pub.publish(msg)
    print('---Published---', msg)
    loop_rate.sleep()

