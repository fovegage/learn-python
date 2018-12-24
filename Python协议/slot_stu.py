# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 14:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : slot_stu.py
# @Software: PyCharm


# 可以节省内存
class A():
    __slots__ = ('name', 'age')


a = A()
a.name = 'Gage'
print(a.name)
