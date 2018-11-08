# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 11:27
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : json_stu.py
# @Software: PyCharm

import json
import os
# loads()：将json数据转化成dict数据
# dumps()：将dict数据转化成json数据
# load()：读取json文件数据，转成dict数据
# dump()：将dict数据转化成json数据后写入json文件

# dumps()：将dict数据转化成json数据
dict = {'a':1, 'b':2}
t = json.dumps(dict)
print(t, type(t), type(dict))

# loads()：将json数据转化成dict数据
l = json.loads(t)
print(l , type(l))

# load()：读取json文件数据，转成dict数据
print(os.getcwd()+'\\a.json')
with open(os.getcwd()+'\\a.json', 'r+', encoding='utf-8') as f:
    # print(f.read())  # str 即json
    print(json.load(f))  # list 即list

# dump()：将dict数据转化成json数据后写入json文件
list = {'page': 'user', 'uri': '/userinfo', 'elements': [{'var_name': 'username', 'description': '登录用户名'}, {'var_name': 'password', 'description': '登录密码'}], 'data': {'userlist': [{'username': '张三', 'password': '******'}, {'username': '李四', 'password': '******'}], 'total': 2}}
print(json.dump())