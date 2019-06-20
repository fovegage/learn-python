# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 14:29
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : match.py
# @Software: PyCharm

import re

# 匹配任意字符 .
# 匹配 .  \.
# 匹配数字 \d
# 匹配单词字符 \w
# 匹配空白字符  \s
# + >=1
# * >=0
# ? 0 or 1


pattern = re.compile(r'\d+')

# 起始位置查找 仅查找一次  match

match1 = pattern.match('hjsal2819kak22ka')
print(match1)
match2 = pattern.match('hjsal2819kak22ka', 5, 20)
print(match2.group())



