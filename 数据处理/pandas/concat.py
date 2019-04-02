# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 17:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : concat.py
# @Software: PyCharm
import pandas as pd
import numpy as np

# 把切分的数据连接起来
d = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [8, 9, 10]]))
d1 = [d[:1], d[2:3]]
print(pd.concat(d1))
