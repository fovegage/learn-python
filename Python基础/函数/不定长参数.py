# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 14:18
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 不定长参数.py
# @Software: PyCharm

# * 表示 元组
# ** 表示 字典


# 直接传入
def a(a, b, *args, **kwargs):
    print(a)  # 1
    print(b)  # 2
    print(args)  # (3, 4)
    print(kwargs) # {'c': 5, 'd': 6}

a(1, 2, 3, 4, c=5, d=6)


# 定义传入
c = (11, 22)
d = {'c':55, 'd':66}
a(77, 88, *c, **d)

print('-'*20)
# 请注意 如果不指定  c d 将认为是元组参数
a(77, 88, c, d)
