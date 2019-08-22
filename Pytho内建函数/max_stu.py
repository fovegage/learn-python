# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 17:19
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : max_stu.py
# @Software: PyCharm

# max  min  *args  iterable
# list首先遍历   lambda 排序规则
print(max(2, 4, 8, 100, 55))
list = [2, 4, 8, 100, 55]
print(max(list, key=str))
# 返回字符串最长的哪个
print(max(list, key=lambda length: len(str(length))))
x = ((3, 5, 8), (3, 8, 5), (3, 6, 9))
print(max(x))
# 只比较下标为 0和2的元素
print(max(x, key=lambda item: (item[0], item[2])))