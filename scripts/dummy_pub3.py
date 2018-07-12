#!/usr/bin/env python

import rospy
from first_smach.msg import State
from time import sleep

rospy.init_node('dummy_pub')
pub = rospy.Publisher('state', State, queue_size=10)
sleep(1)

msg = State()
msg.statename = 'Hoge'
msg.id = 'Hoge1'
msg.src = ['success', 'failed']
msg.dst = ['Foo1', 'Recovery']
msg.is_end = False
pub.publish(msg)
sleep(1)
msg = State()
msg.statename = 'Foo'
msg.id = 'Foo1'
msg.src = ['success', 'failed']
msg.dst = ['Hoge2', 'Recovery']
msg.is_end = False
pub.publish(msg)
sleep(1)
msg = State()
msg.statename = 'Hoge'
msg.id = 'Hoge2'
msg.src = ['success', 'failed']
msg.dst = ['Foo2', 'Recovery']
msg.is_end = False
pub.publish(msg)
sleep(1)
msg = State()
msg.statename = 'Foo'
msg.id = 'Foo2'
msg.src = ['success', 'failed']
msg.dst = ['success', 'Recovery']
msg.is_end = False
pub.publish(msg)
sleep(1)
msg = State()
msg.statename = 'Recovery'
msg.id = 'Recovery'
msg.src = ['success', 'failed']
msg.dst = ['Hoge1', 'failed']
msg.keywords = ['sleeptime']
msg.args = ['3']
msg.is_end = True
pub.publish(msg)
print('---Published---', msg)
sleep(1)
print('Press Ctrl-C to terminate.')
while not rospy.is_shutdown():
    pass
