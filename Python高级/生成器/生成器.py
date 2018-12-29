# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 13:03
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 生成器.py
# @Software: PyCharm


# 生成器   即可迭代对象
list = [x for x in range(6)]  # 返回一个列表  iterable
print(list)


it = (x for x in range(6))  # 返回一个对象 iterator
print(it)
print(next(it))
print(next(it))

