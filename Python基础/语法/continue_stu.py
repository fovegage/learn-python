# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:31
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : continue_stu.py
# @Software: PyCharm


# 将过滤 w 输出其他
str = 'hello world'
for s in str:
    if s == "w":
        continue
    print(s)

# 将过滤 5 输出其他
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)