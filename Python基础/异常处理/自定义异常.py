# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 18:39
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 自定义异常.py
# @Software: PyCharm

class DefineExcept(Exception):
    def __init__(self, length, least):
        self.length = length
        self.least = least

try:
    s = input()
    if len(s) < 3:
        raise DefineExcept(len(s), 3)
except DefineExcept as ret:
    print('至少输入{}个字符, 你输入了{}个字符'.format(ret.least, ret.length))
else:
    print('无异常')