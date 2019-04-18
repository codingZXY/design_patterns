# -*- coding: utf-8 -*-
# @Time  : 2019/4/18
# @Author : ethan

from abc import ABCMeta,abstractmethod

class FlyBehavior(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying with my beautiful wings.")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly.")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket.")
