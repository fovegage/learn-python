# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:02
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : pool_stu.py
# @Software: PyCharm

from multiprocessing import Pool
import time
import random
import os


def work(msg):
    start = time.time()
    print("work{}开始执行,id为{}".format(msg, os.getpid()))
    time.sleep(random.random()*2)
    stop = time.time()
    print("work{}耗时{}.".format(msg, stop-start))

p = Pool()
for i in range(10):
    # 非堵塞运行
    p.apply_async(work, args=(i,))
    # 堵塞进行
    # p.apply(work, args=(i,))


print("开始")
p.close()
p.join()
print("结束")

# 注意进程号，释放后可复用，具体取决于操作系统调度
"""
开始
work0开始执行,id为20541
work1开始执行,id为20542
work3开始执行,id为20544
work2开始执行,id为20543
work1耗时0.920670747756958.
work4开始执行,id为20542
work3耗时1.7335271835327148.
work0耗时1.9560186862945557.
work5开始执行,id为20544
work2耗时1.966829776763916.
work6开始执行,id为20541
work7开始执行,id为20543
work5耗时0.21103501319885254.
work8开始执行,id为20544
work4耗时1.839451551437378.
work9开始执行,id为20542
work6耗时0.8850796222686768.
work8耗时1.2740142345428467.
work9耗时0.911503791809082.
work7耗时1.9466755390167236.
结束
"""