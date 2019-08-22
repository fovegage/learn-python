# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 14:49
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : zip_stu.py
# @Software: PyCharm

# zip  iter --> tuple
list1 = [1, 2, 3, 5]
list2 = [4, 5, 6]
zipped = zip(list1, list2)
# print(list(zipped))  # 为节省内存   返回obj  list取出 [(1, 4), (2, 5), (3, 6)]
# print(list(zip(*zipped)))  # [(1, 2, 3), (4, 5, 6)]

for name, value in zipped:
    print(name, value)
