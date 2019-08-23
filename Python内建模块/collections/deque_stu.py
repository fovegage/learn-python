#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:deque_stu.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 12:19   
@Version:1.0
'''

from collections import deque

# deque 队列实现

# 可以直接放入可迭代对象
s = 'hello'
de = deque(s)
print(de)
de.appendleft('d')
print(de)
de.append('w')
print(de)

# 指定队列长度,队列长度为3，多插入不会报错
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

