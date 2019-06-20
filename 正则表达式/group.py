# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 14:34
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : group.py
# @Software: PyCharm

import re

p = re.compile(r'(\d+).(\d+)')

# group 指的是 正则表达式的分组 分几组就能group()几个
# group() == group(0)
se = p.search('hdadah212l21dd')
print(se.group())  # 匹配内容
