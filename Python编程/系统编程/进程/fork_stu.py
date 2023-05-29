# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 10:59
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : fork_stu.py
# @Software: PyCharm

import os
import time

# 注意，fork函数，只在Unix/Linux/Mac上运行，windows不可以

pid = os.fork()

# 子进程返回的pid一定是0
if pid == 0:
    print('哈哈1')

# fork() 调用一次，返回两次  一个返给父进程  一个返给子进程
else:
    print('哈哈2')

print("*" * 50)

num = 0

pid = os.fork()

# fork()函数是直接复制的父进程的所有数据，因此数据互不影响

if pid == 0:
    num += 1
    print('哈哈1---num=%d' % num)
else:
    time.sleep(1)
    num += 1
    print('哈哈2---num=%d' % num)
