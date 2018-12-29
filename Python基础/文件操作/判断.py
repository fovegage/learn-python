# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 15:57
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 判断.py
# @Software: PyCharm

import os, sys

# 打开文件
fd = os.open( "E:\\test.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
os.write(fd, b"This is test")

# 使用 isatty() 查看文件
ret = os.isatty(fd)   # 如果文件打开返回 True

print(ret)

# 关闭文件
os.close(fd)