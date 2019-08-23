# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 16:37
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : hashlib_stu.py
# @Software: PyCharm

import hashlib

md5 = hashlib.md5()
md5.update('hello'.encode('utf-8'))
print(md5.hexdigest())
print(md5.digest())

print(chr(98))