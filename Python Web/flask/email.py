# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 10:15
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : ls.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_script import Manager, Shell
from flask_mail import Mail, Message
from threading import Thread
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '602556194@qq.com'
app.config['MAIL_PASSWORD'] = 'cihfqwwiybyhbbfa'
mail = Mail(app)

msg = Message('标题', sender='602556194@qq.com', recipients=['sdgaozhe@163.com'])
msg.body = '内容'
with app.app_context():
    mail.send(msg)

if __name__ == '__main__':
    app.run()
