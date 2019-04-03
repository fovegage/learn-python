# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 16:51
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : time_stu.py
# @Software: PyCharm

from datetime import time

'dst', 'fold', 'hour', 'isoformat', 'max', 'microsecond', \
'min', 'minute', 'replace', 'resolution', 'second', \
'strftime', 'tzinfo', 'tzname', 'utcoffset'

# 需要自己构造  此模块一般不会用到
t = time(20, 23, 6, 382)

# 格式化时间
print(t.isoformat())

# 替换时间
print(t.replace(13))

# value
print(t.max)
print(t.resolution)
print(t.min)
