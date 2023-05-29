# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 11:25
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 线程公用.py
# @Software: PyCharm

import asyncio
import threading


@asyncio.coroutine
def hi():
    print(threading.current_thread())
    yield from asyncio.sleep(1)
    print(threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hi(), hi()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
