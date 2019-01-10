# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 10:32
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 引入.py
# @Software: PyCharm


# 引入消费者生产者的模型 一个生产 一个消费

def custumer():
    r = ''
    while True:
        n = yield r  # 接受send的值  返出yield的值
        if not n:
            return
        print('custer {}'.format(n))
        r = 'done'

def produce(c):
    c.send(None)  # 启动
    n = 0
    while n < 5:
        n += 1
        print('custer {}'.format(n))
        r = c.send(n)
        print('custer return {}'.format(r))
    c.close()

c = custumer()
produce(c)