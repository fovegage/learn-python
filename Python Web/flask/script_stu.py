# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 11:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : script_stu.py
# @Software: PyCharm
from flask import Flask, request
from  flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return 'flask-script测试'

if __name__ == '__main__':
    manager.run()