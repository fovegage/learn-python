# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 16:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : super_Stu3.py
# @Software: PyCharm

# 重写
class A:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, item):
        return getattr(self.obj, item)

    def __setattr__(self, key, value):
        if str(key).startswith('_'):
            super().__setattr__(key, value)
        else:
            setattr(self.obj, key, value)