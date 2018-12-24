# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 14:56
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 简化.py
# @Software: PyCharm

class Struc():
    _fields = []

    def __init__(self, *args):
        if len(self._fields) != len(args):
            raise TypeError('must is {}'.format(len(args)))
        else:
            for name, value in list(zip(self._fields, args)):
                setattr(self, name, value)

class Point(Struc):
    _fields = ['name', 'age']


p = Point('Gage', 24)
print(p.__dict__)
print(vars(p))