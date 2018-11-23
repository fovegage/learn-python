# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 10:01
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : property_stu.py
# @Software: PyCharm

# 将方法转换为只读
# 重新实现一个属性的设置和读取方法,可做边界判定
class Money(object):
    def __init__(self):
        self.__money = 8


    def getMoney(self):
        return self.__money


    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

    money = property(getMoney, setMoney)

print(Money().getMoney())
print(Money().money)

class MoneyA():
    def __init__(self):
        self.__money = 8

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('Error')

print(MoneyA().money)
