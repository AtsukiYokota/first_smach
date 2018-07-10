#!/usr/bin/env python

import rospy
from smach import State, StateMachine

from random import random
from time import sleep

class Hoge(State):
    def __init__(self, **kwargs):
        self.sleeptime = 1
        try:
            self.sleeptime = int(kwargs['sleeptime'])
        except KeyError:
            pass

        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        print('Hoge')
        sleep(self.sleeptime)
        if random() > 0.6:
            print('Hoge:[success]')
            sleep(self.sleeptime)
            return 'success'
        else:
            print('Hoge:[failed]')
            sleep(self.sleeptime)
            return 'failed'


class Foo(State):
    def __init__(self, **kwargs):
        self.sleeptime = 1
        try:
            self.sleeptime = int(kwargs['sleeptime'])
        except KeyError:
            pass
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        print('Foo')
        sleep(self.sleeptime)
        sleep(self.sleeptime)
        if random() > 0.6:
            print('Foo:[success]')
            sleep(self.sleeptime)
            return 'success'
        else:
            print('Foo:[failed]')
            sleep(self.sleeptime)
            return 'failed'


class Recovery(State):
    def __init__(self, **kwargs):
        self.sleeptime = 1
        try:
            self.sleeptime = int(kwargs['sleeptime'])
        except KeyError:
            pass
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        print('Recovery')
        sleep(self.sleeptime)
        if random() > 0.3:
            print('Recovery:[success]')
            sleep(self.sleeptime)
            return 'success'
        else:
            print('Recovery:[failed]')
            sleep(self.sleeptime)
            return 'failed'


