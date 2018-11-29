# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 14:01
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : context_stu.py
# @Software: PyCharm

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