# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 14:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : spilt.py
# @Software: PyCharm

import re

a = 'kdsslllslsl'
b = 'h52177jsal2819kak22ka'
pattern = re.compile(r'\d+')
# spilt 分割
# 以匹配的内容进行分割，比 str.spilt() 更强大
# return list
spilt = pattern.split(a)
print(spilt)

str1 = 'hell3kkk7ojjjaja7jjj'
print(str1.split('a'))
