# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 18:15
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 静态方法.py
# @Software: PyCharm


class Person():

    @staticmethod
    def name():
        print('hello')

p = Person()
p.name()  #对象调用
Person.name()  # 实列调用