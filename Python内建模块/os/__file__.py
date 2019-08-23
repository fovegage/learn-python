# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 14:45
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : __file__.py
# @Software: PyCharm

import sys

print(sys.path)

# 如果当前文件包含在sys.path里面，那么，__file__返回一个相对路径！
# 如果当前文件不包含在sys.path里面，那么__file__返回一个绝对路径！
print(__file__)