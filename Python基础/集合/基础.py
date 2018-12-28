# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 18:05
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 基础.py
# @Software: PyCharm

# 集合元素不可重复

list = [1, 4, 4, 6]
print(set(list))

set = {1, 4, 6}
set.update([1, 3])
print(set)