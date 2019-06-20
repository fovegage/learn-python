# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 13:59
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : search.py
# @Software: PyCharm

import re

pattern = re.compile(r'\d+')
# 全局查找 仅查找一次 相当于贪婪模式
search = pattern.search('hjsal2819kak22ka')
print(search.group())

# 属性
print(search.start()) # 开始位置
print(search.end())  # 结束位置
print(search.span())  # 跨越位置

