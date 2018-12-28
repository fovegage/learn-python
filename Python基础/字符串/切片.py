# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:38
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 切片.py
# @Software: PyCharm

# 切片语法  [index:end:step]
# 若不指 end 和 step  将从index处遍历到
# 取值区间 [)  左闭右开
str = 'hello'

print(str[0:3:2]) # hl

print(str[1:])  # ello

print(str[::-1])  # olleh 逆序

print(str[::1])  # hello 正向步长 正序

print(str[1:-1]) # ell

