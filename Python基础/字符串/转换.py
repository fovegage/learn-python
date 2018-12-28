# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:53
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 转换.py
# @Software: PyCharm

# expandtabs()  '\t'转为空格  可指定空格数
str = 'hello\tworld'
print(len(str.expandtabs(tabsize=36)))
print(str.expandtabs(tabsize=36))
