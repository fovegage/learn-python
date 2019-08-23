# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 11:30
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : reduce.py
# @Software: PyCharm

import functools
from functools import reduce

# print(dir(functools))


print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

print(list(filter(lambda x: x%2==0,range(10))))
