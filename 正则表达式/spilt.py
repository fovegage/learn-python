# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 14:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : spilt.py
# @Software: PyCharm

import re

pattern = re.compile(r'\d+')
# spilt 分割
# 以匹配的内容进行分割，比 str.spilt() 更强大
# return list
spilt = pattern.split('kskks19291ll12lll1ss1gg')
print(spilt)


str1 = 'hell3o'
print(str1.split('3'))