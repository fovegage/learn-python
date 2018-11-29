# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 11:31
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : call_stu.py
# @Software: PyCharm

class A():
    def __call__(self, a):
        self.a = a
        print(self.a)

    def print(self):
        print(self.a)

t = A()
t(5)

t.print()

class Entity():

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''改变实体的位置'''
        self.x, self.y = y, x
        print(self.x, self.y)

e = Entity(3, 4, 3)
e.__call__(3, 5)






