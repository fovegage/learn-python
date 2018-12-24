# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 17:39
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : sorted_stu.py
# @Software: PyCharm

# sorted  reverse key

list = [1, 55, 244, 7, 3]
print(sorted(list, reverse=True))
print(sorted(list, key=lambda x: len(str(x))))