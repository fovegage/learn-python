# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 11:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : class_stu.py
# @Software: PyCharm

class person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = person('Gage', 24)
print(p.age)

