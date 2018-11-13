# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 11:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : Python方法.py
# @Software: PyCharm

#  静态方法   实例方法  类方法

# 静态方法  即在类中不加参数  无需实例化可以直接被调用
class People():
    countury = "china"

    @staticmethod
    def getContury():
        print(People.countury)

People().getContury()

# 静态类

class Student():
    name = "Gage"

    @classmethod
    def getName(cls):
        return cls.name

print(Student.getName())

class Student():
    name = "Gage"

    @classmethod
    def getName(cls):
        return cls.name

    @classmethod
    def setName(cls, name):
        cls.name = name

s = Student()
s.setName('Fovegage')
print(s.getName())