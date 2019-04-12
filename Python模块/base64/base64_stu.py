# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 16:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : base64_stu.py
# @Software: PyCharm

import base64

# 二进制编码
s = b'hello'
a = base64.b64encode(s)
print(a)
print(base64.b64decode(a))

# "url safe"的base64编码，其实就是把字符+和/分别变成-和_
url = b'i\xb7\x1d\xfb\xef\xff'
c = base64.b64encode(url)
print(c)
d = base64.urlsafe_b64encode(url)
print(d)
