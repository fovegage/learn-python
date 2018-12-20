# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 16:09
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : property_stu3.py
# @Software: PyCharm

# 属性变成方法
class Area():
    def __init__(self, radious):
        self.radious = radious

    @property
    def a(self):
        return self.radious * 3

    @property
    def a(self):
        return self.radious * 6

a = Area(6)
print(a.a)