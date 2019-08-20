#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:defaultdict_stu.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 14:15   
@Version:1.0
'''
from collections import defaultdict

# 创建类似于倒排索引的字典对象

d = [('yellow', 1), ('blue', 3), ('yellow', 6), ('blue', 4)]

f = defaultdict(list)

for key, value in d:
    # 它继承了list，所以具有append()方法
    f[key].append(value)

print(f.items())

# 统计字符出现的次数
s = 'abaskskaaaa'

f = defaultdict(int)

for i in s:
    # 如果没有该遍历的键，则创建，如果有进行赋值操作
    f[i] += 1

print(f.items())


# 自定义工厂

# 返出一个 object 对象
def costom_factory(value):
    return lambda: value

f = defaultdict(costom_factory('hi'))
f.update(name='Gage', age=18)

print('%(name)s %(age)s to %(object)s' % f)