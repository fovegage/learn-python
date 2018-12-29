# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 14:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : stu.py
# @Software: PyCharm

import types

class Perosn():

    def __init__(self, name):
        self.name = name



def eat(self):
    print(self.name + '在吃东西')

p = Perosn('老王')
p.eat = types.MethodType(eat, p)
p.eat()