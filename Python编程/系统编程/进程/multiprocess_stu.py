# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 11:43
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : multiprocess_stu.py
# @Software: PyCharm

import os
import time
from multiprocessing import Process


def dance(name):
    print("子进程{}, id为{}.".format(name, os.getpid()))


if __name__ == '__main__':
    print('当前进程为{}.'.format(os.getpid()))
    p = Process(target=dance, args=("dance",))
    print("子进程开始执行")
    # 不设置默认 Process-1 开始
    print(p.name)
    # 若无 target参数 则在调用start()的时候会自动调用run(), 有则调用指定的函数
    p.start()
    p.join()
    print("子进程执行结束")

"""
当前进程为14096.
子进程开始执行
子进程dance, id为5664.
子进程执行结束
"""


# 主进程的时间   包含子进程运行的时间
# 子进程要执行的代码
def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s,age=%d ,pid=%d...  《%s》' % (name, age, os.getpid(), i))
        print(kwargs)
        time.sleep(0.5)


if __name__ == '__main__':
    print('父进程 %d.' % os.getpid())
    p = Process(target=run_proc, name="modi_name", args=('test', 18), kwargs={"m": 20})
    print('子进程将要执行')
    p.start()
    print(p.name)
    # 等待子进程 一秒  就停止   在for内的是一个进程 由外部控制
    time.sleep(1)
    p.terminate()
    p.join()
    print('子进程已结束')

"""
父进程 14552.
子进程将要执行
子进程运行中，name= test,age=18 ,pid=44828...  《0》
{'m': 20}
子进程运行中，name= test,age=18 ,pid=44828...  《1》
{'m': 20}
子进程已结束
"""
