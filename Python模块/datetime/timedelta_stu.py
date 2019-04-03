# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 17:13
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : timedelta_stu.py
# @Software: PyCharm

from datetime import timedelta, datetime


'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds'

now = datetime.now()

offsetday = now + timedelta(days=34)
print(offsetday)



