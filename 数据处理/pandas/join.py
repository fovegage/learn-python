# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 17:51
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : join.py
# @Software: PyCharm

import pandas as pd

left = pd.DataFrame({'key': ['Apple', 'Orange'], 'value': [9.9, 8.8]})
right = pd.DataFrame({'key': ['Apple', 'Orange'], 'value': [6.9, 4.8]})

print(pd.merge(left, right, on='key'))


left = pd.DataFrame({'key': ['Apple', 'Apple'], 'value': [9.9, 8.8]})
right = pd.DataFrame({'key': ['Apple', 'Apple'], 'value': [6.9, 4.8]})

print(pd.merge(left, right, on='key'))