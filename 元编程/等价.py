# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 14:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 等价.py
# @Software: PyCharm

# 下面的片段效果是一样的 只不过第一种更加简洁
class A:
    @classmethod
    def add(cls):
        pass

class B:
    def add(self):
        pass
    method = classmethod(add)