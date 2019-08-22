# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 16:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : range_stu.py
# @Software: PyCharm


# 为了节约内存  返回的不是列表  需要用 list 取到
a = range(10)
print(list(a))


# [start:end:step]
b = range(1, 10, 2)
print(list(b))

# 取负值  和 切片思想一致
c = range(-1, -10, -1)
print(list(c))