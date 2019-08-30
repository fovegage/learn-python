#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:create.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/22 11:21   
@Version:1.0
'''

# 关键字创建
info = dict(name='Gage', sex='man')
print(info)

# 二元元组创建
info = [('name', 'Gage'), ('sex', 'man')]
print(dict(info))

# zip 创建
info = dict(zip(('name', 'sex'), ('Gage', 'man')))
print(info)

# 列表推导式创建
info = {i: i + 1 for i in range(3)}
print(info)

# fromkeys()
info = dict.fromkeys(range(1, 13), '1')
print(info)

# 特殊
# 用下标
l = ['x', 1, 'y', 2, 'z', 3]
info = dict(zip([x for x in l if l.index(x) % 2 == 0], [x for x in l if l.index(x) % 2 != 0]))
print(info)
# 用切片
info = dict(zip(l[::2], l[1::2]))
print(info)

