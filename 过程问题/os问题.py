# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 16:48
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : os问题.py
# @Software: PyCharm

import os
import io

# io.open()是文件I / O的首选高级接口。它将操作系统级文件描述符包装在一个对象中，您可以使用该对象以Pythonic方式访问该文件。
# os.open()只是较低级别的POSIX系统调用的包装器。它需要较少的符号(和更多POSIX-y)参数，并返回表示打开的文件的文件描述符(一个数字)。它不返回文件对象;返回的值将不具有read()或write()方法。
# 文件描述符对象
# site: https://baike.baidu.com/item/%E6%96%87%E4%BB%B6%E6%8F%8F%E8%BF%B0%E7%AC%A6
f1 = os.open('F:\\test.txt', os.O_RDONLY)
print(f1)

# 外存操作 返回文件对象
f2 = open('F:\\test.txt')
print(f2)

# 内存操作 返回文件对象
f3 = io.open('a.txt', 'w')
print(f3.write('jdj'))
