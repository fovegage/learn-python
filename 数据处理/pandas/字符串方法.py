# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 17:29
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 字符串方法.py
# @Software: PyCharm
import pandas as pd
import numpy as np

s = pd.Series(['Python', 'Java', 'C', 'C++', 'GoLang', 'R', 'Ruby'])
print(s.str.upper())  # 这里和Python内置的字符串方法就一直了