# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 17:53
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 多继承.py
# @Software: PyCharm


# 定义驴
class A():
    def test(self):
        print('我是母驴')

# 定义马
class B():
    def test(self):
        print('我是公马')

# 定义骡子
class C(A, B):
    def __str__(self):
        print('我继承了马和驴')

c = C()
c.test()
print(C.__mro__)    # 继承顺序
