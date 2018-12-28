# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 15:55
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 分割.py
# @Software: PyCharm

str = 'C:\\Program Files\\National Instruments\\MAX'
print(str.split('\\'))
print(str.split('\\', 2))  # 最多按 \\ 分割两次


str = 'hello\n world'
print(str.splitlines())
print(str.splitlines(True))

str = 'I love you'
print(str.partition('love'))