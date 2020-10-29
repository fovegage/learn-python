# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 15:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 工厂模式.py
# @Software: PyCharm


# 首先定义一个抽象基类
class CarStore(object):

    # 定义生产汽车的方法
    def createcar(self, name):
        pass

    # 根据类型去生产车
    def order(self, name):
        self.car = self.createcar(name)
        self.car.move()


# 定义4s店  实现抽象类
class AoDiCarStore(CarStore):

    def createcar(self, name):
        self.factory = CarFactory()
        return self.factory.createcar(name)


# 创建一个车
class AoDi():

    def move(self):
        print('移动')


# 定义一个工厂
class CarFactory():

    def createcar(self, name):
        self.name = name
        if self.name == 'AoDi':
            self.car = AoDi()

        return self.car


aodi = AoDiCarStore()
aodi.order('AoDi')
