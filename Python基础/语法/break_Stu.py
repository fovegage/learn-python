# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:27
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : break_Stu.py
# @Software: PyCharm

# 将输出 w 之前的内容
str = 'hello world'
for s in str:
    if s == "w":
        break
    print(s)


# 同理他将输出 5 之前的内容
i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print(i)