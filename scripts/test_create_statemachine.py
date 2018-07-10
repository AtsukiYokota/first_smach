#!/usr/bin/env python

import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer
from test_states import Hoge, Foo, Recovery
from first_smach.msg import State

flag = True
statemachine = StateMachine(outcomes=['success', 'failed'])

def tuples_to_dict(keys, values):
    transition = {}
    for key, value in zip(keys, values):
        transition[key] = value
    return transition

def callback(message):
    global flag
    global statemachine
    if flag:
        kwargs = {}
        if message.keywords:
            print('=======keywords:{}, args:{}========='.format(message.keywords, message.args))
            kwargs = tuples_to_dict(message.keywords, message.args)
            print('#######kwargs:{}#########'.format(kwargs))
        with statemachine:
            StateMachine.add(message.id, globals()[message.statename](**kwargs), \
            transitions=tuples_to_dict(message.src, message.dst))
        if message.is_end is True:
            flag = False
            sis = IntrospectionServer('server_name', statemachine, '/SM_ROOT')
            sis.start()
            statemachine.execute()

if __name__ == '__main__':
    rospy.init_node('create_statemachine')
    sub = rospy.Subscriber('state', State, callback)
    rospy.spin()

