# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 17:19
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 实例方法.py
# @Software: PyCharm


# 明确 p.hello() 其实就是 hello(p,)  self 用来表明类本身
class Perosn():
    def hello(self):
        print('hello')

p = Perosn()
p.hello()
# Perosn.hello()  错误