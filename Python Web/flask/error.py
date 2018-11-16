# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 11:53
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : error.py
# @Software: PyCharm
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return 'flask-script测试'

if __name__ == '__main__':
    app.run()