# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 21:27
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : mongo.py
# @Software: PyCharm
import pymongo


def mongo():
    client = pymongo.MongoClient("localhost", 27017)
    db = client.pay
    return db

sign = mongo().payinfo.find_one({'payid': '1f044782fa2311e889a5b252164282bf'})
print(type(sign))


print(sign['payid'])
# # info = []
# # for i in sign:
# #     info.append(i['subject'])
# #     info.append(i['body'])
# #     info.append(i['fee'])
# #     info.append(i['orderid'])
# #
# # print(info[0])
#
# # for i in [i['subject'] for i in sign]:
# #     print(i)
#
# print([i['subject'] for i in sign][0])