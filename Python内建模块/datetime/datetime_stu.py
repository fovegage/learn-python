# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 11:43
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : datetime_stu.py
# @Software: PyCharm

import time
from datetime import datetime

'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromordinal', \
'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond',\
'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime',\
'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', \
'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year'

# Construct function

# 首先构造时间类
# 计算机时间
dt = datetime.fromtimestamp(time.time())
print(datetime.now())

# 格林威治时间
udt = datetime.utcfromtimestamp(time.time())
print(datetime.utcnow())

# 按指定日期和时间构建时间类
from datetime import time
print(datetime.combine(dt, time(20, 12, 8)))

# 2019-04-03 17:08:46.611102+08:00 时区
print(dt.astimezone())

# Wed Apr  3 17:09:54 2019
print(dt.ctime())

# 2019-04-03
print(dt.date())

print(dt.fold)


# 2019-04-02 15:45:19.924590
print(datetime.now())

# 可以直接加减
d1 = datetime.strptime('2018-07-11 17:41:20', '%Y-%m-%d %H:%M:%S')
# d2 = datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.now()
delta = d2 - d1
print(delta.days)
print(delta)
