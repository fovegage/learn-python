# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 17:57
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 迭代器生成器.py
# @Software: PyCharm


# 这是一个迭代器
L = [x*x for x in range(10)]
print(L)


# 这是一个生成器
L = (x*x for x in range(10))
print(L)
print(next(L))  # 只有生成器才可以使用next() 或 __next__