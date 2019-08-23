# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 10:18
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : io_stu.py
# @Software: PyCharm

from io import BytesIO, StringIO

from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('Word')
print(f.getvalue())
#getvalue()方法用于获得写入的str


