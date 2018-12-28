# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 13:45
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 匹配.py
# @Software: PyCharm

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