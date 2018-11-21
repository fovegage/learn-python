# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 14:29
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : re_stu.py
# @Software: PyCharm

import re

# 判断是否匹配
re.match(r'^[aeiou]', str)

# 以第二个参数指定的字符替换原字符串中内容
re.sub(r'^[aeiou]', '?', str)
re.sub(r'(xyz)', r'\1', str)

# 编译生成独立的正则表达式对象
expr = re.compile(r'^...$')
expr.match(...)
expr.sub(...)