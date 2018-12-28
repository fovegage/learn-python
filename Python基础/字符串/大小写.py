# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 13:52
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 大小写.py
# @Software: PyCharm

str = 'hello'

# capitalize()  仅第一个字符大写，其余小写
print(str.capitalize())

# casefold() lower() 全部转换为小写  casefold()为加强版  支持语言更多
print(str.casefold())

# lower  全部转换为小写
print(str.lower())

# upper  全部转换为大写
print(str.upper())


# title()  转为大写开头    capitalize() 只转第一个   title 转每个单词开头的第一个
str = 'dTg'
print(str.title())

S = "this is string example....wow!!!"
print(S.swapcase())

S = "This Is String Example....WOW!!!"
print (S.swapcase())
