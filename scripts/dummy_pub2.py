#!/usr/bin/env python

import rospy
from first_smach.msg import State

rospy.init_node('dummy_pub')
pub = rospy.Publisher('state', State, queue_size=10)


names = ('Hoge', 'Foo', 'Recovery')
srcs = [('success', 'failed'), ('success', 'failed'), ('success', 'failed')]
dsts = [('Foo', 'Recovery'), ('Hoge', 'Recovery'), ('Hoge', 'failed')]
loop_rate = rospy.Rate(1)

while not rospy.is_shutdown():
    msg = State()
    msg.name = 'Hoge'
    msg.src = ['success', 'failed']
    msg.dst = ['Foo', 'Hoge']
    msg.is_end = False
    pub.publish(msg)
    msg = State()
    msg.name = 'Foo'
    msg.src = ['success', 'failed']
    msg.dst = ['success', 'Recovery']
    msg.is_end = False
    pub.publish(msg)
    msg = State()
    msg.name = 'Recovery'
    msg.src = ['success', 'failed']
    msg.dst = ['Hoge', 'failed']
    msg.keywords = ['sleeptime']
    msg.args = ['3']
    msg.is_end = True
    pub.publish(msg)
    print('---Published---', msg)
    loop_rate.sleep()

