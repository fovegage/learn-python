# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 15:59
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 读写.py
# @Software: PyCharm

from io import StringIO

f = StringIO()

f.write('hello')

print(f.getvalue())

f.close()