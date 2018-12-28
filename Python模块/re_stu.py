# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 14:29
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : re_stu.py
# @Software: PyCharm

import re

# 字符串前面加 r 表示原生
# 使用 compile() 函数将正则表达式的字符串形式编译为一个 Pattern 对象
# 通过 Pattern 对象提供的一系列方法对文本进行匹配查找，获得匹配结果，一个 Match 对象。
# 最后使用 Match 对象提供的属性和方法获得信息，根据需要进行其他的操作

# import
# 匹配任意字符 .
# 匹配 .  \.
# 匹配数字 \d
# 匹配单词字符 \w
# 匹配空白字符  \s
# + >=1
# * >=0
# ? 0 or 1
pattern = re.compile(r'\d+')

# 起始位置查找 仅查找一次  match
match1 = pattern.match('hjsal2819kak22ka')
print(match1)
match2 = pattern.match('hjsal2819kak22ka', 5, 20)
print(match2.group())

# 全局查找 仅查找一次
search = pattern.search('hjsal2819kak22ka')
print(search.group())

# 属性
print(search.start()) # 开始位置
print(search.end())  # 结束位置
print(search.span())  # 跨越位置

# 全部找出来 findall  返回list
findall = pattern.findall('h52177jsal2819kak22ka')
print(findall)

# 全部找出来 返回迭代器
finditer = pattern.finditer('h52177jsal2819kak22ka')
print(finditer)

# spilt 分割
# return list
spilt = pattern.split('kskks19291ll12lll1ss')
print(spilt)

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

# 中文匹配
title = u'你好，hello，世界'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(title)
print(result)

