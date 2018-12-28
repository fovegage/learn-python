# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 16:51
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 添加.py
# @Software: PyCharm

list = ['a', 'b', 'c']

# 尾部添加
list.append('d')
print(list)

# 指定位置添加
list.insert(2, 'hello')
print(list)

# 遍历添加可迭代对象
list.extend(['1', '2'])
print(list)