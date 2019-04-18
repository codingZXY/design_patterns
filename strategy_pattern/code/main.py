# -*- coding: utf-8 -*-
# @Time  : 2019/4/16
# @Author : ethan

import ducks
import fly_behavior as fb

def print_something_between_func(text='-'):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(text.center(50, '-'))
            func(*args,**kwargs)
            print('-'.center(50, '-'))

        return wrapper
    return decorator

@print_something_between_func('mallard_duck')
def play_with_mallard_duck():
    mallard_duck = ducks.MallardDuck()
    mallard_duck.display()
    mallard_duck.perform_quack()
    mallard_duck.perform_fly()

@print_something_between_func('rubber_duck')
def play_with_rubber_duck():
    rubber_duck = ducks.RubberDuck()
    rubber_duck.display()
    rubber_duck.perform_quack()
    rubber_duck.perform_fly()

@print_something_between_func('model_duck')
def play_with_model_duck():
    model_duck = ducks.ModelDuck()
    model_duck.display()
    model_duck.perform_quack()
    model_duck.perform_fly()
    model_duck.set_fly_behavior(fb.FlyRocketPowered()) #动态设置飞行行为
    model_duck.perform_fly()


if __name__ == '__main__':
    play_with_mallard_duck()
    play_with_rubber_duck()
    play_with_model_duck()

