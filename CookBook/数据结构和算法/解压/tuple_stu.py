#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:tuple_stu.py
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 10:14   
@Version:1.0
'''

# 在Python中，注意args会对元组进行自动封装
# 应该注意的是对于单个数据类型，在进行声明元组类型时，我们应该用 逗号 进行声明
a = 4,
b = (4,)
print(a is b)

x = 4, 5
y = (4, 5)
print(x is y)
