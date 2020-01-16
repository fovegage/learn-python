# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 11:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : super_stu.py
# @Software: PyCharm

# 和Java一样  子类实列化  父类也实例化   反之不可以
# 继承父类的参数使用super
# 这里应该和重载和重写区分

"""
作用一 ：继承抽取工作属性，同时子类可以有自己的行为
"""


class Person():
    def __init__(self, name):
        self.name = name
        self.age = 18


class Student(Person):
    def __init__(self, name, skill):
        super().__init__(name) # 保证父类初始化
        self.skill = skill

    def print(self):
        print(self.name + " " + str(self.age) + self.skill)


p = Student('Gage', "Dance")
p.print()
