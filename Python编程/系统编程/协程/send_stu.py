# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 10:25
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : send_stu.py
# @Software: PyCharm

def gen():
    i = 0
    while i < 5:
        a = yield i
        print(a)
        i += 1

# for i in gen():
#     print(i)


f = gen()
print(f.send(None))
print(f.send('hello'))
print(f.send('world'))