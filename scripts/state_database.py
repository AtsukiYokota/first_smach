#!/usr/bin/env python

import rospy
from smach import State, StateMachine

from random import random
from time import sleep

class PartsRecognition(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        pass
        return 'success'


class Planning(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        pass
        return 'success'


class HandMoving(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        pass
        return 'success'


class GraspCheck(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        pass
        return 'success'


class Positioning(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        pass
        return 'success'


class HogeOperation(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        pass
        return 'success'

