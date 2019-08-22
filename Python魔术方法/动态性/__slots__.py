# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 14:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : __slots__.py
# @Software: PyCharm


# 1、可以节省内存； 2、只有在 slots 里面的属性才可被调用，使其失去动态性
class A:
    __slots__ = ('name', 'age')


a = A()
a.name = 'Gage'
# a.sex = 'man'  # 这里会报属性错误
print(a.name)


# 可以被类动态绑定
class B:
    pass


b = B()
b.sex = 'man'
print(b.sex)
