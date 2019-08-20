#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:args_stu.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 10:30   
@Version:1.0
'''

# 在对基本的数据类型进行解压后，我们发现，如果一个数据类型非常长，而我们只需要个别元素
# 此时我们可以对数据元素进行相应的封装

info = ['Gage', 66, 88, (1994, 7, 15)]
# 我们只需要出生日期
*args, date = info
print(date)


# 延伸到函数,在这里你可以感受到 * 相当于C语言的指针，它可以取出相应的元素

def func1(info):
    print(*info)


func1(info)


# 关于单独的 * 取出的元素，默认是list类型
def func2(info):
    name, *num, date = info
    print(num, type(num))


func2(info)

# 对于不规则的元素

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print(s)

# 动态的进行遍历解压
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    if tag == 'bar':
        do_bar(*args)
