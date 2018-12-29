# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 17:20
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : next_stu.py
# @Software: PyCharm

# next
it = iter([1, 2, 3, 4, 5])
# iterator  不
#可len()
while True:
    try:
        x = next(it)
        print(x, end=',')
    except StopIteration:
        break
# default
for i in range(6):
    print(next(it,'juge'))