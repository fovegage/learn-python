# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : time_stu.py
# @Software: PyCharm

import time
from datetime import datetime
print(datetime.now())
# time.sleep(5) # 延时

print(time.strftime('%Y-%m-%d %H-%M-%S'))


d1 = datetime.strptime('2018-07-11 17:41:20', '%Y-%m-%d %H:%M:%S')
# d2 = datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.now()
delta = d2 - d1
print(delta.days)
print(delta)