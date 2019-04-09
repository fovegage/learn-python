# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 16:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : base64_stu.py
# @Software: PyCharm

import base64

s = 'oooo'
b = base64.b64decode(s)
print(b)

be = base64.b64decode('YWJjZA==')
print(be)

# url = base64.urlsafe_b64decode('+')

print('呵呵'.encode('ascii'))