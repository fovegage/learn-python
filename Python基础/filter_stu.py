# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 16:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : filter_stu.py
# @Software: PyCharm

def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))