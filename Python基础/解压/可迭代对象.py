# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 15:58
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 可迭代对象.py
# @Software: PyCharm

# 安规律过滤
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
print(line.split(':'))
name, *filed, home, list = line.split(':')
print(name, home, list)

# 序列循环拆分

reco = [
    ('a', 1, 2),
    ('b', 'hello'),
    ('a', 3, 4)
]

def a(x, y):
    print(x, y)

def b(s):
    print(s)

for key, *value in reco:
    if key == 'a':
        a(*value)
    else:
        b(*value)