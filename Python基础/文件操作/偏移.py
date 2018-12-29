# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 15:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 偏移.py
# @Software: PyCharm

# seek() / tell()
f = open('E:\\test.txt', 'r')
content = f.readline()
print(content)
f.seek(1, 0)   # offset 需要移动的字节数   whence： 0 开头 1 当前 2 末尾
print(f.tell())  # 获取指针位置
content = f.readline()  # 再次读取将有移动一位读取
print(content)
f.close()
