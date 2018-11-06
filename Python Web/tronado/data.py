# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 15:46
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : data.py
# @Software: PyCharm

from pymongo import MongoClient

client = MongoClient('localhost',27017)
print(client)