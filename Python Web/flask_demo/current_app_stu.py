# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 11:50
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : current_app_stu.py
# @Software: PyCharm

from flask import Flask, current_app

app = Flask(__name__)

# ctx
ctx = app.app_context()
ctx.push()
a = current_app
print(a)
ctx.pop()