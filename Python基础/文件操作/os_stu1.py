# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 15:32
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : os_stu1.py
# @Software: PyCharm

import os


print(os.getcwd())  # 当前目录
os.chdir('E:\\')  # 切换目录
print(os.getcwd())  # 已经更改
print(os.listdir()) # 获取目录 列表
print(os.getlogin())  # 获取登录用户名
# print(os.mkdir())  # 创建目录

# os.F_OK: 作为access()的mode参数，测试path是否存在。
# os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读
# os.W_OK 包含在access()的mode参数中 ， 测试path是否可写
# os.X_OK 包含在access()的mode参数中 ，测试path是否可执行

print(os.access('G:\\91', os.F_OK))  # 可用于判断


# 指定相应的文件名
# os.rename("E:\\test.txt", "E:\\testtest.txt")  # 重命名
# os.remove("E:\\test.txt") # 删除