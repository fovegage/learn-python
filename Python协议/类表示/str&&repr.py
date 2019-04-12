# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 11:24
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : str&&repr.py
# @Software: PyCharm


# __repr__() 生成的文本字符串标准做法是需要让 eval(repr(x)) == x 为真
class A():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return ('Pair({0.x!r}, {0.y!r})'.format(self))

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

a = A(3, 5)
print(a)