# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : os_stu.py
# @Software: PyCharm

import os

# os.getcwd()  # 当前目录
# os.chdir()  # 切换目录
# os.listdir() # 获取目录 列表
#
# os.rename()  # 重命名
# os.remove() # 删除

# 当前
ls = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"..")
print(ls)


# 添加
import os
path = "E:\\ls"  # 自动添加
b = os.path.join(path,"abc")
print(b)