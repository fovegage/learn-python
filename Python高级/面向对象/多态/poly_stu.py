# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 17:25
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : poly_stu.py
# @Software: PyCharm

# 多态：同一种事物的多种形态，动物分为人类，猪类（在定义角度）
# 多态性：一种调用方式，不同的执行效果（多态性）
class Animal():
    def run(self):
        return AttributeError("该方法必须实现")


class Pig(Animal):
    def run(self):
        print('pig running')

class Cat(Animal):
    def run(self):
        print('cat running')



p = Pig()
p.run()


def func(obj):
    obj.run()

func(p)