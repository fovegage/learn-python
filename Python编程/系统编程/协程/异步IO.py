# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 11:27
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 异步IO.py
# @Software: PyCharm

import asyncio

@asyncio.coroutine
def wget(host):
    print('wait wget {}'.format(host))
    # 写
    connect = asyncio.open_connection(host, 80)
    render, writer = yield from connect
    hender =  'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(hender.encode('utf-8'))
    yield from writer.drain()
    # 读
    while True:
        content = yield from render.readline()
        if content == b'\r\n':
            break
        print(content)
    writer.close()


loop = asyncio.get_event_loop()
site = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(site))



