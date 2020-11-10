# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 16:46
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : re_url.py
# @Software: PyCharm
from werkzeug.routing import BaseConverter
from flask import Flask, url_for
app = Flask(__name__)

# # 自定义正则转换器
# class RegexConverter(BaseConverter):
#     def __init__(self, url_map, *args):
#         super(RegexConverter, self).__init__(url_map)
#         # 将接受的第1个参数当作匹配规则进行保存
#         self.regex = args[0]
#
# app.url_map.converters['re'] = RegexConverter
#
# @app.route('/index/<re("\S+"):nid>')
# # @app.route('/index/item.html?a=3')
# def index(nid):
#     return nid

@app.route('/login')
def login():
    return 'login'

with app.test_request_context():
    print(url_for('login'))
    print(url_for('login', a=2))


if __name__ == '__main__':
    app.run(port=5003, debug=True)