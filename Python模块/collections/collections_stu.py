# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 13:53
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : collections_stu.py
# @Software: PyCharm

from collections import Counter, deque, OrderedDict, defaultdict, Sequence

d = {'2': 3, '3': 2, '17': 2, '3': 2, '17': 2, 'y': 8}
print(Counter(d))

# 若作为可迭代对象 则以元组统计可迭代元素出现的次数  若为dict则  去重且排序输出
s = "abcdhaaksllaaa"
cl = Counter(s)
print(cl)  # 返回列表
print(cl['a'])  # 列表取值
print(cl.most_common(3))  # 按出现顺序的前三个
print(list(cl.elements()))  # 返回迭代器 列表取出
print(' '.join(sorted(cl.elements())))
print(cl.update('hhwh6'))
print(cl)

# deque 队列实现

s2 = 'ksalla'
de = deque(s2)
print(de)
de.appendleft('d')
print(de)
