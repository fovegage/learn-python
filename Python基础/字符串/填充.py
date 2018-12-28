# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 13:47
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 填充.py
# @Software: PyCharm

# ljust()/rjust() 填充  包含字符串位数
str = 'python'
print(str.ljust(7, "#"))


# 字符串居中 以*填充  长50  不指定则为空白
print(str.center(50))
print(str.center(50, '*'))
