# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 16:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : enumerate_stu.py
# @Software: PyCharm

num = ['one', 'two', 'three', 'four']
enum =  enumerate(num)
print(enum)  # 节约内存 返回可迭代对象
print(list(enum))

# [(0, 'one'), (1, 'two'), (2, 'three'), (3, 'four')]
