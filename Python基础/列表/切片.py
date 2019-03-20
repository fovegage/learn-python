# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 16:03
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 切片.py
# @Software: PyCharm

"""
:param list[start, stop, step]  start default 0  stop default len(list)
note: if start < stop step default is 1 else step default is -1
"""

# 调用内建函数  slice()
num_list = [1, 2, 3, 4, 5]
# start > stop and step >=0  return []
print(num_list[5: 3])
# start > stop and step <0  return [5]
print(num_list[5: 3: -1])

# start < stop and step >=0  return [4, 5]
print(num_list[3: 5])


print(num_list[3: 5: -1])  # []
print(num_list[::-2])  # 如果步长 >= -1 l列表倒序输出
print(num_list[::-1])  # 倒序步长默认为 -1
print(num_list[::1])  # 正序步长默认为 1

my = slice(1, 5, -1)
print(my)
print(num_list[my])
reversed()