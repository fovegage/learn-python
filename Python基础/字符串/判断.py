# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 14:45
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 判断.py
# @Software: PyCharm


# islower  仅对字母判断
str = 'hello'
print(str.islower())


# isalnum()   判断是否由数字和字母组成
str = 'jjjssss22'
print(str.isalnum())

# isalpha() 判断只有字母  26个字母以外均报错
str = 'sjsksk'
print(str.isalpha())

# isdecimal()  若全部是十进制数返回true  否则false
demo = '1234'
print(demo.isdecimal())

# isidentifier() 是否是python标识符  由字母、数字、下划线组成  且不能以数字开头
str = '90'
print(str.isidentifier()) # False

# islower() 是否全部是小写
str = 'Tskksks'
print(str.islower())  # False

# isdigit()  是否全部是数字
num = '999'
print(num.isdigit())

# isspace() 若是空格或制表符返回True  其他均false  注意 '' 和 ' '是不一样的
str = '\t'
print(str.isspace())

# istitle() 判断是否是大写开头
str = 'dTg'
print(str.istitle())

# 若全部是数字返回true   isdigit()的加强版  支持'²3455'
s = '\u00B23455'
print(repr(s))
print(s.isnumeric())