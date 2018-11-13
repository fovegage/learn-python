# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 22:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : __new__stu.py
# @Software: PyCharm

class inch(float):
    def __new__(cls, args):
        return float.__new__(cls, args*3)

print(inch(12))