# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:12
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 无参数.py
# @Software: PyCharm
from functools import wraps
# 无参数
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

print(test1())