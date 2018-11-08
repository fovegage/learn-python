# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 17:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : sys_stu.py
# @Software: PyCharm

# os.path 是一个模块，用来处理目录、路径相关的模块
# sys.path 是一个列表，返回解释器相关的目录列表、环境变量、注册表等初始化信息

import sys
import os
print(os.path)
print("*"*999)
print(sys.path)  # 获取全部

print(sys.argv[0]) # 接受外界值

sys.stdout.write('hello' + '\n')
print('hello')  # 调用上面一行

# 输出到文件 重定向
f_handler=open('out.log', 'w')
sys.stdout=f_handler
print('hello')

import sys
print('Plase input your name: ')
name = sys.stdin.readline()
print(name)