# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 16:37
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 浅.py
# @Software: PyCharm

import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

b = a  #赋值，传对象的引用


# c = copy.copy(a)  #对象拷贝，浅拷贝
# d = copy.deepcopy(a)  #对象拷贝，深拷贝
# a.append(5)  #修改对象a
# a[4].append('c')  #修改对象a中的['a', 'b']数组对象
# print(a)
# print(b)
# print(c)
# print(d)


l1 = [1, 2, [3, 4]]
l2 = copy.deepcopy(l1)
l1.append(5)
l1[2].append(5)
print(l1)
print(l2)