# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 11:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : super_stu.py
# @Software: PyCharm

# 和Java一样  子类实列化  父类也实例化   反之不可以
# 继承父类的参数使用super
# 这里应该和重载和重写区分
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
