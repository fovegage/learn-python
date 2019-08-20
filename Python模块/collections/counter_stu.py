#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:counter_stu.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 12:57   
@Version:1.0
'''

from collections import Counter

# 统计可迭代对象出现的次数

# 字典
d = {'2': 3, '3': 2, '17': 2, '3': 2, '17': 2, 'y': 8}
print(Counter(d))  # Counter({'y': 8, '2': 3, '3': 2, '17': 2}) 注意输出

# str
# 若作为可迭代对象 则以元组统计可迭代元素出现的次数  若为dict则  去重且排序输出
s = "abcdhaaksllaaa"
cl = Counter(s)
print(cl)  # 返回列表
print(cl['a'])  # 列表取值
print(cl.most_common(3))  # 按出现顺序的前三个
print(list(cl.elements()))  # 返回迭代器 列表取出
print(' '.join(sorted(cl.elements())))
cl.update('ahhwh6')  # 更新数值，内存地址不变
print(cl)
