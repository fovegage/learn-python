# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 9:51
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 截取.py
# @Software: PyCharm


# truncate()  必须有写属性   因为截取删除
f = open('E:\\test.txt', 'r+')
content = f.read()
print(content)
f.truncate(8)  # 截取8的字节   不指定 截取全部
f.close()
