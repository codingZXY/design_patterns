# -*- coding: utf-8 -*-
# @Time  : 2019/4/18
# @Author : ethan

from abc import ABCMeta,abstractmethod
import fly_behavior as fb
import quack_behavior as qb

class Duck(metaclass=ABCMeta):
    fly_behavior = None
    quack_behavior = None

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self,fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self,quack_behavior):
        self.quack_behavior = quack_behavior

    def swim(self):
        print('All ducks float.')

class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = fb.FlyWithWings()
        self.quack_behavior = qb.Quack()

    def display(self):
        print("I'm a mallard duck, my head color is Green")

class RedHeadDuck(Duck):
    def __init__(self):
        self.fly_behavior = fb.FlyWithWings()
        self.quack_behavior = qb.Squeak()

    def display(self):
        print("I'm a red head duck, my head color is Red")

class RubberDuck(Duck):
    def __init__(self):
        self.fly_behavior = fb.FlyNoWay()
        self.quack_behavior = qb.Squeak()

    def display(self):
        print("I'm a rubber duck, I like swimming in the tub.")

class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = fb.FlyNoWay()
        self.quack_behavior = qb.MuteQuack()

    def display(self):
        print("I'm a model duck, I can do nothing. Try to change my behaviors.")