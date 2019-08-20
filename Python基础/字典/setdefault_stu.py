#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:setdefault_stu.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 15:10   
@Version:1.0
'''

d = [('yellow', 1), ('blue', 3), ('yellow', 6), ('blue', 4)]

ds = {}

for key, value in d:
    ds.setdefault(key, []).append(value)

print(ds.items())
