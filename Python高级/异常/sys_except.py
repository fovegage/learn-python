# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 14:32
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : sys_except.py
# @Software: PyCharm

import sys

# 使用 sys 获取异常
try:
    1/0
except:
    types, value, back= sys.exc_info()
    sys.excepthook(types, value, back)
