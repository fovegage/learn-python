# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 15:52
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : date_stu.py
# @Software: PyCharm

from datetime import date
import time

'ctime', 'day', 'fromordinal', 'fromtimestamp', 'isocalendar', \
'isoformat', 'isoweekday', 'max', 'min', 'month', 'replace', 'resolution', \
'strftime', 'timetuple', 'today', 'toordinal', 'weekday', 'year'

# Constructors:
# 2019-04-02 time() -> struct_time(y, m, d)  可指定
print(date.fromtimestamp(time.time()))

# 今天
print(date.today())

# 此方法一般用不到，西方农历
print(date.fromordinal(99))

# Methods:
# ctime()
# Wed Oct  9 00:00:00 2019
date1 = date(2019, 10, 9)
print(date1.ctime())

# 格式化时间
print(date1.strftime('%Y-%m-%d'))

# isocalendar
# (2019, 41, 3)   年 第几周 周几
print(date1.isocalendar())

# 'YYYY-MM-DD' print
print(date1.isoformat())

# 周几
print(date1.isoweekday())

# 替换现在的日期
print(date1.replace(2021, 10, 7))

# return struct_time 结构化时间
print(date1.timetuple())

#  Gregorian ordinal time 西方农历
print(date1.toordinal())
print(date.fromordinal(date1.toordinal()))

# Properties:
# today = date.today()
# print(today.year, today.month, today.day)
#
#
# # value
# print(date.max)  # 9999-12-31
# print(date.min)  # 0001-01-01
# print(date.resolution) # 日期单位
