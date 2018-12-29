# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 17:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : issubclass_stu.py
# @Software: PyCharm

# issubclass() 判断是不是子类
class D():
    a = 1
class E(D):
    b = 2
print(issubclass(E, D))