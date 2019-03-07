# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 11:55
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : test.py
# @Software: PyCharm
import requests
import hashlib
import urllib
# ret = requests.get('http://127.0.0.1:12346/pay/oosl')
# print(ret.text)

pay_data = {
    # 'appid': '6',
    'out_trade_no': '882199199119kkss',
    'total_fee': '9.1',
    'subject': '宏基电脑',
    'body': '测试商品',
}

# info = {}
#
# def sort_list():
#     for i in sorted(pay_data):
#         info[i] = pay_data[i]
#     return info
#
# # 进行连接
# para = urllib.parse.urlencode(sort_list())
# # print(para)
# # send = para + '&key=gAQfCJxHwcJrLFxcmX2Kr6fStKBB3Mrx'
# m1 = hashlib.md5()
# m1.update(para.encode("utf-8"))
# token = str(m1.hexdigest()).upper()
# pay_data['sign'] = token

# print(pay_data)
ret1 = requests.post('http://127.0.0.1:11111/add', data=pay_data)
print(ret1.text)
import pymongo
# def mongo():
#     client = pymongo.MongoClient("localhost", 27017)
#     db = client.pay
#     return db
#
# print(mongo().payinfo.find_one({'orderid': ''}))