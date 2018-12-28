# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:56
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 查找.py
# @Software: PyCharm


# count 搜索字符串 搜不到返回0  搜到大于1  从1起始  可以指定搜索范围
master = 'hello'
sub = 'p'
print(master.count(sub, 1, 5))

# find  可指定起始位置  查到返回位置  查不到 -1
str = 'fovegage'
print(str.find('a'))

# index   可指定起始位置  查到返回位置  若子字符串不存在或不在指定范围内 会异常
print(str.index('e'))