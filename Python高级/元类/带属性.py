# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 15:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 带属性.py
# @Software: PyCharm


foo = type('Foo', (), {'a': 3})

print(foo.a)