# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 14:05
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : find.py
# @Software: PyCharm

import re

a = 'kdsslllslsl'
b = 'h52177jsal2819kak22ka'

pattern = re.compile(r'\d+')
# 全部找出来 findall  返回list
findall = pattern.findall(b)
print(findall)

# 全部找出来 返回迭代器
finditer = pattern.finditer(a)
print(finditer)

# 中文匹配
# unicode编码, 一种全世界语言都包括的一种编码

title = u'你好，hello，世界'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(title)
print(result)
