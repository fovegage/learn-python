# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 14:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : sub.py
# @Software: PyCharm
import re

# sub 替换
p = re.compile(r'(\w+) (\w+)')
s = 'hello 123, hello 456'
repl = p.sub(r'hello world', s)
print(repl)

# ‘\1’ 匹配的是 所获取的第1个()匹配的引用
# ‘\2’ 匹配的是 所获取的第2个()匹配的引用
# 例如，’(\d)\1’ 匹配两个连续数字字符。如33aa 中的33
gro = p.sub(r'\2 \1', s)
print(gro)


# 使用函数

# 将 s 传入 match
def func(m):
    # print(m.group(2))
    return 'hi' + ' ' + m.group(2)


print(p.sub(func, s))
