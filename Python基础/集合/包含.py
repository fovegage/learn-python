# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 18:38
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 包含.py
# @Software: PyCharm

# 和 子集一致
x = {"f", "e", "d", "c", "b"}
y = {"e", "b", "c"}

z = x.issuperset(y)

print(z)