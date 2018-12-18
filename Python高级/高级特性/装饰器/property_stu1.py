# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 10:01
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : property_stu1.py
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

# print(Money().getMoney())
# print(Money().money)


# 装饰器实现
class MoneyA():
    def __init__(self):
        self.__money = 8

    @property  # 即getter方法
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('Error')

a = MoneyA()
print(a.money)
a.money = 100
print(a.money)


# 不可修改
class Bank():
    def __init__(self):
        self.__money = 1000

    @property
    def account(self):
        return self.__money

b = Bank()
print(b.account)
# a.money = 100  # 这是错误的