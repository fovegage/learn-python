# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : for_stu.py
# @Software: PyCharm


list = ['a', 'b', 'c']

for i in list:
    print(i)


# 不建议这样操作  时间复杂度为 o(n)
for i in range(len(list)):
    print(list[i])