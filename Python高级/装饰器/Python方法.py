# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 11:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : Python方法.py
# @Software: PyCharm

#  静态方法   实例方法  类方法

# 静态方法  即在类中不加自身参数self  无需实例化可以直接被调用
class People():
    countury = "china"

    @staticmethod
    def getContury():
        print(People.countury)

# People().getContury()

# 静态类
# 不加self  但必须加cls  若调用类内方法  cls() 需要实例化
# 调用无需实例化
class Student():
    name = "Gage"

    def sayHello(self):
        print('hello')

    @classmethod
    def getName(cls):
        c= cls()
        return cls.name, c, c.sayHello()

print(Student.getName())


# 修改类内属性值
class Student():
    name = "Gage"

    @classmethod
    def getName(cls):
        return cls.name

    @classmethod
    def setName(cls, name):
        cls.name = name

s = Student()
# s.setName('Fovegage')
print(s.getName())