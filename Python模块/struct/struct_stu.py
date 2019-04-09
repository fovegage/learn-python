# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 16:52
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : struct_stu.py
# @Software: PyCharm

import struct
import base64
print(bytes(10240099))

bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

print(str(bmp_header))

print(struct.unpack('<ccIIIIIIHH', bmp_header))

n = 10240099
print((n & 0xff000000) >> 24)