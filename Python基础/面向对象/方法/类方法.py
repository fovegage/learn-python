# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 18:08
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 类方法.py
# @Software: PyCharm


class Person():

    name = 'Gage'

    @classmethod
    def getName(cls):
        print(cls.name)

p = Person()
p.getName()