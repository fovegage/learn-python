# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 14:56
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : str_Stu.py
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

    # 可以利用 str 直接获取
    def __str__(self):
        return self.name + ' ' + str(self.age)

p = Point('Gage', 24)
print(p.__dict__)
print(vars(p))
print(p)