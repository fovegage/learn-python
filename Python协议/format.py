# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 11:37
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : format.py
# @Software: PyCharm

_format = {
    'ymd': '{f.year}-{y.month}-{y.day}',
    'dmy': '{f.day}/{y.month}/{y.year}'
}

class Date():
    def __init__(self):
        pass

    def __format__(self, format_spec):
        pass