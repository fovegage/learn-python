# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 14:45
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : file.py
# @Software: PyCharm

# 必须实现 __init__  __del__ 若传出 __str__
# __new__、__init__、

class FileOperate():
    def __init__(self, path, name):
        self.file = open(path+name, 'r')

    def __str__(self):
        return self.file.read()

    def __del__(self):
        self.file.close()
        del self.file

file = FileOperate('F:\\', 'l1.txt')
print(file)



