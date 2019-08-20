#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:list_stu.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 10:21   
@Version:1.0
'''

# 需要注意，解压个数应该与列表长度相同
data = ['Hello', 12, 66, (1, 2, 3)]
x, y, z, k = data

a, b, c = k
print(a, b, c)

# 占位，对于不想要的数据我们可以使用 _ 进行占位
a, _, c = k
print(a, c)

# 计算平均值，去掉一个最高分和最低分

scores = [66, 87, 98, 82, 69, 91, 77]
scores.sort()
less, *mid, more = scores
print(sum(mid) / len(mid))


