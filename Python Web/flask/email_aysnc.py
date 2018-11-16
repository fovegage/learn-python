# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 10:22
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : email_aysnc.py
# @Software: PyCharm

from flask import Flask, request
from flask_mail import Mail, Message
from threading import Thread


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '602556194@qq.com'
app.config['MAIL_PASSWORD'] = 'cihfqwwiybyhbbfa'

mail = Mail(app)

# 异步发送邮件
def send_async_mail(app, msg):
    mail = Mail(app)
    with app.app_context():
        mail.send(msg)

# 多线程
@app.route('/')
def mail():
    msg = Message('标题', sender='602556194@qq.com', recipients=['sdgaozhe@163.com', 'sdgaozhe@qq.com'])
    msg.body = '内容'
    msg.html = '<b>test</b>'
    thread = Thread(target=send_async_mail, args=(app, msg))
    thread.start()
    return 'success'

if __name__ == '__main__':
    app.run()