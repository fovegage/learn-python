# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 17:50
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 遍历.py
# @Software: PyCharm


dict = {'name': 'Gage', 'age': 18}

# items 以元组返回  对应拆分
print(dict.items())

for key, value in dict.items():
    print(key, value)

