# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 14:01
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : context_stu.py
# @Software: PyCharm

# 上下文管理器 yield之前的代码会在  __enter__ 中进行 而若异常则在 __exit__ 进行
import time
from contextlib import contextmanager
@contextmanager
def test_contetx():
    start= time.time()
    try:
        yield
    finally:
        end = time.time()
        print('it cost {}'.format(end-start))

with test_contetx():
    time.sleep(10)


@contextmanager
def list_trans(orgin_list):
    trans = list(orgin_list)
    yield trans
    orgin_list[:] = trans

item = [1, 2, 3]
with list_trans(item) as add:
    add.append(4)

print(item)


