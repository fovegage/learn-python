# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 9:49
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : group.py
# @Software: PyCharm

# 如果是 dict  key为columns  value为value

import numpy as np
import pandas as pd

d = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar'],
    'B': ['one', 'two', 'three', 'four'],
    'C': np.random.randn(4),
    'D': np.random.randn(4)
})

print(d.groupby('A').sum())

print(d.groupby(['A', 'B']).sum())