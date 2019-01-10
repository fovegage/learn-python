# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 11:05
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : asyncio_stu.py
# @Software: PyCharm

import asyncio

@asyncio.coroutine
def hello():
    print('hello world')
    yield from asyncio.sleep(1)  # 等待完成
    print('hello again')


loop = asyncio.get_event_loop()   # 获取时间循环
loop.run_until_complete(hello())  # 等待全部完成
loop.close()

