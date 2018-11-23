# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 11:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : super_stu.py
# @Software: PyCharm

class Person():
    def __init__(self, name):
        self.name = name
        self.age = 18

class Student(Person):
    def __init__(self, name):
        # self.skill = skill
        super().__init__(name)

    def print(self):
        print(self.name + " " + str(self.age))

p = Student('Gage')
p.print()