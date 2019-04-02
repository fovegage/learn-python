# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 9:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : append.py
# @Software: PyCharm

# 将一行添加

import numpy as np
import pandas as pd

d = pd.DataFrame(np.random.rand(8, 4), columns=list('ABCD'))

i3 = d.iloc[3]

d1 = d.append(i3, ignore_index=True)

print(d1)
print(id(d), id(d1))  # 注意和list append不一样