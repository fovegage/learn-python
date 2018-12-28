# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 16:55
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 查找.py
# @Software: PyCharm

list = ['a', 'b', 'c']

# in
if 'a' in list:
    print("True")

# index   [sub:start:end]  不存在异常
print(list.index('b', 0, 4))

# count 不存在返回 0
print(list.count('b'))

