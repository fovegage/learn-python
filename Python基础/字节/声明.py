# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 18:13
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 基础.py
# @Software: PyCharm

# 为了适应国际化编码
# 所有方法和 str 一致
# 字符串是以字符为单位进行处理
# bytes类型是以字节为单位处理的
# 文本总是Unicode，由str类型表示，二进制数据则由bytes类型表示

# 字节
byte = b'hello'
print(byte)

# 字符串
str = '你好'
print(type(str))

# 字符串转换
bytes = bytes('你好', encoding='utf-8')
print(type(bytes), bytes)