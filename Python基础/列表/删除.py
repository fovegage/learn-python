# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 17:00
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 删除.py
# @Software: PyCharm

list = ['a', 'b', 'c']

# del  指定删除
del list[1]
print(list)

# pop  尾部删除
list.pop()
print(list)

# remove  删除值
list.remove('a')
print(list)