# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 11:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : class_stu.py
# @Software: PyCharm

class person():

    color = 'yellow'

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = person('Gage', 24)
p.sex = 'man'
print(p.age)
print(p.sex)  # 定义和color一样的属性
print(p.color)

print(vars(p))


