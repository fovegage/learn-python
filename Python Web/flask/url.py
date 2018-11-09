# encoding: utf-8

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    login_url = url_for('login')
    return redirect(login_url)
    return u'这是首页'


@app.route('/login/')
def login():
    return u'这是登陆页面'


@app.route('/question/<is_login>/', url_for('question', a=2))
def question(is_login):
    if is_login == '1':
        return u'这是发布问答的页面'
    else:
        print(url_for('login', a=2))
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=5009, debug=True)
