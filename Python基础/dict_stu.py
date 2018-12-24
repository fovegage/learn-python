# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 15:15
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : dict_stu.py
# @Software: PyCharm

l = dict(a=3, b=4)
print(l)

keys = ('name', 'age')
dict = dict.fromkeys(keys, )
print(dict)

def ls(**kwargs):
    for name, expected_type in kwargs.items():  # items()   遍历元组  下面拆开
        print(name, expected_type)

n = {'name':str, 'shares':int, 'price':float}
ls(name=str, shares=int, price=float)
