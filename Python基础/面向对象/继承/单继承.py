# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 11:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 单继承.py
# @Software: PyCharm


class Animal():

    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name + '会跑')


class Person(Animal):

    def setName(self, name):
        self.name = name

    def program(self):
        print(self.name + "在编程")

p = Person('Gage')
p.setName('Fovegage')   # 会现在子类查找  查找不到到父类
p.program()