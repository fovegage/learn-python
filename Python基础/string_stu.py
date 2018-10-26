# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 11:21
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : String__stu.py
# @Software: PyCharm

str = 'hello Wo\trld'

# capitalize()  仅第一个字符大写，其余小写
print(str.capitalize())

# casefold() lower() 全部转换为小写  casefold()为加强版  支持语言更多
print(str.casefold())

# lower  全部转换为小写
print(str.lower())

# islower  仅对字母判断
print(str.islower())

# 字符串居中 以*填充  长50  不指定则为空白
print(str.center(50))
print(str.center(50, '*'))

# encode   默认utf-8   可指定  编码
# decode  解码
print(str.encode())

# endswith   可指定起始位置
# return  false/true
print(str.endswith('d'))
print(str.endswith('d', 1, 3))

# expandtabs()  '\t'转为空格  可指定空格数
print(str.expandtabs(tabsize=36))

# count 搜索字符串 搜不到返回0  搜到大于1  从1起始  可以指定搜索范围
sub = 'h'
print(str.count(sub))
print(str.count(sub, 1, 5))

# find  可指定起始位置  查到返回位置  差不多 -1
print(str.find('p'))

# index   可指定起始位置  查到返回位置  若子字符串不存在或不在指定范围内 会异常
print(str.index('h'))

# format
print("我爱你{}.".format('中国'))
list = ['我', '爱', '你']
print("{0[0]}{0[1]}{0[2]}中国".format(list))
dict = {'name': 'china'}
print("{name}".format(**dict))
# 变量替换
demo = 'Gage has {num} messages.'
print(demo.format(num=38))

# format_mat
point = {'x':4, 'y':5}
print('{x}, {y}'.format_map(point))

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
print(str.isidentifier())

# islower() 是否全部是小写
str = 'Tskksks'
print(str.islower())

# isdigit()  是否全部是数字
num = '999'
print(num.isdigit())

# 若全部是数字返回true   isdigit()的加强版  支持'²3455'
s = '\u00B23455'
print(repr(s))
print(s.isnumeric())

# isprintable()  若是空格或是可打印的字符串则 true  注意 制表符不可打印
str = 'python)))\t'
print(str.isprintable())

# isspace() 若是空格或制表符返回True  其他均false  注意 '' 和 ' '是不一样的
str = '\t'
print(str.isspace())

# istitle() 判断是否是大写开头
str = 'dTg'
print(str.istitle())

# title()  转为大写开头    capitalize() 只转第一个   title 转每个单词开头的第一个
str = 'dTg'
print(str.title())

# join 拆分可迭代对象
str1 = 'love'
str2 = '123'
print(str1.join(str2))
list = ['1', '2', '3']
op = ','
print(op.join(list))

# ljust()/rjust() 填充  包含字符串位数
str = 'python'
print(str.ljust(7, "#"))

# lstrip/rstrip  截取开头或结尾字符串
str = 'hello'
print(str.lstrip(''))




