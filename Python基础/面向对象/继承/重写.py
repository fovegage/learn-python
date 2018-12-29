# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 17:58
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 重写.py
# @Software: PyCharm

class Anmial():
    def say(self):
        print('我是动物')

class Person(Anmial):
    def say(self):
        print('我是码畜')

p = Person()
p.say()