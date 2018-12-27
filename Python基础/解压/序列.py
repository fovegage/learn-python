# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 15:50
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 序列.py
# @Software: PyCharm

# 元组
p = (4, 5)
x, y = p
print(x, y)

# 混合 / 占位
group = ['AMCE', 4, {'a':1}, True, (2018, 12, 9)]
# a, b, c, d, e = group
_, b, c, _, e = group
year, month, day = e
print(year, month, day)

# 字符串
s = 'hello'
f, g, f, j, k = s
print(f)
