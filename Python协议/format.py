# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 11:37
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : format.py
# @Software: PyCharm

_format = {
    'ymd': '{f.year}-{f.month}-{f.day}',
    'dmy': '{f.day}/{f.month}/{f.year}'
}

class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _format[format_spec]
        return fmt.format(f=self)

d = Date(2018, 10, 1)
print(format(d))
print(format(d, 'dmy'))
