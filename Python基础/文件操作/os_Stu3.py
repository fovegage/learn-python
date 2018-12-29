# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 16:58
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : os_Stu3.py
# @Software: PyCharm

import os

# 获取文件名
print(os.path.basename(__file__))

# 当前路径
ls = os.path.abspath(os.path.dirname(os.getcwd()))
print(ls)
print(os.getcwd())

# a.py  返回文件名
print(os.path.basename('D:\\Users\\foveg\\AppData\\a.py'))

# 不包括文件的路径
print(os.path.dirname('D:\\Users\\foveg\\AppData\\a.py'))

# 绝对路径
print(os.path.abspath('D:\\Users\\foveg\\AppData\\a.py'))


