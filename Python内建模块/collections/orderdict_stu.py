#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:orderdict_stu.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 14:15   
@Version:1.0
'''
from collections import OrderedDict

# 构建所有value均相同的字典结构
d = OrderedDict.fromkeys('abcde', '12345')
print(d)
# 把对应的key移动到开头或结尾
d.move_to_end('d', last=False)
print(d)

# orderdict 记住字典插入的顺序

sign_data = {'a': 12, 'e': 11, 'b': 77}

print(OrderedDict(sign_data))

# 它会记住字典的重构顺序
print(OrderedDict(sorted(sign_data.items())))
