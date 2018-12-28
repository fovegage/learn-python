# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 17:15
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : fromkeys_stu.py
# @Software: PyCharm

l = dict(a=3, b=4)
print(l)

keys = ('name', 'age')
dict = dict.fromkeys(keys, )
dict['name'] = "Gage"
dict['age'] = 18
print(dict)
