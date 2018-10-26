# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 11:53
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : reduce_stu.py
# @Software: PyCharm

from functools import reduce

print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
