# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 17:03
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : n1.py
# @Software: PyCharm

import numpy as np

arr = np.array([[[1, 2, 3], [8, 9, 12]], [[1, 2, 4], [2, 4, 5]]])  # 2*2*3
print(arr.cumsum(0))
# print(arr.cumsum(1))
# print(arr.cumsum(2))
