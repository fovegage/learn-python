# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 11:23
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : expect_stu.py
# @Software: PyCharm

try:
    open('hello')
except IOError:
    print('文件不存在')


try:
    print(num)
except NameError as ret:
    print(ret)


try:
    f = open('E:\\test.txt')
    try:
        con = f.read()
        print(con)
    except IOError as ret:
        print(ret)
    finally:
        f.close()
except:
    print('文件不存在')