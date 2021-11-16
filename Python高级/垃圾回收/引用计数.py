# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 15:48
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 引用计数.py
# @Software: PyCharm

import sys
import gc

# 请在Python解释器下运行  为 2  创建一次 调用一次
str1 = 'hello world'
print(sys.getrefcount(str1))


class ClassA():
    def __init__(self):
        print('object born,id:%s' % str(hex(id(self))))
    # def __del__(self):
    #     print('object del,id:%s'%str(hex(id(self))))


def f3():
    print("-----0------")
    # print(gc.collect())
    c1 = ClassA()
    c2 = ClassA()
    c1.t = c2
    c2.t = c1
    print("-----1------")
    del c1
    del c2
    print("-----2------")
    print(gc.garbage)
    print("-----3------")
    print(gc.collect())  # 显式执行垃圾回收
    print("-----4------")
    print(gc.garbage)
    print("-----5------")
    print(gc.get_count())


if __name__ == '__main__':
    """
    什么是引用技术 
    a = 1
    b = a
    
    这样 1 同时指向 a b  
    只有 当  del a  和  del b  python 才会进行gc回收
    
    """
    gc.set_debug(gc.DEBUG_LEAK)  # 设置gc模块的日志
    f3()
