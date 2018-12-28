# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 17:18
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 删除.py
# @Software: PyCharm

# 删除 key
dict = {'name': 'Gage', 'age': 18, 'sex':'man'}
del dict['age']
print(dict)

# 清空
dict.clear()
print(dict)