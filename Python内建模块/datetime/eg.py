# -*- encoding: utf-8 -*-

# @File:eg.py
# @Author:fovegage
# @Contact:fovegage@gmail.com
# @Created Time:2019/9/2 15:32   
# @Version:1.0

import calendar
from datetime import date

year = date.today().year
month = date.today().month

# 每月的最后一天
print(date(year, month, calendar.monthrange(year, month)[1]))

# 每月的第一天
print(date(year, month, 1))
