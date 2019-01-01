# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : random_stu.py
# @Software: PyCharm

import random

print(random.randint(1, 7))  # [a, b]  生成随机整数

print(random.random())   # [0, 1)  在 0 到 1 范围生成随机数

print(random.uniform(1, 5))  # [a, b]指定范围生成随机浮点数

print(random.randrange(1, 10, 2))  # 在 1 3 5 7 9 随机选一个

print(random.choice(range(1, 10, 2)))  # 在 序列中随机选择一个  与上面等效

print(random.choices(5))

