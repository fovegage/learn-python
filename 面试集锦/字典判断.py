# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 17:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 字典判断.py
# @Software: PyCharm

dict1 = {'name': 'Gage', 'age': 20, 'sex': '男'}

t = (((key, value) for key, value in dict1.items() if key=='name'))
print(dict(((key, value) for key, value in t)))





