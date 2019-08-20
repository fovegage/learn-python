#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:namedtuple.py
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 14:16   
@Version:1.0
'''

from collections import namedtuple

# 坐标点计算
Point = namedtuple('Point', ['x', 'y'])
p = Point(x=11, y=33)
print(p[0] + p[1])
print(p.x + p.y)

print(p._make([1, 3]))
