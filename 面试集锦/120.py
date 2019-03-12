# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-


# 作用域
num = 5


def func():
    global num
    num = 4


func()
print(num)

# 字典更新
name = {'name': 'Gage'}
age = {'age': 25}

name.update(age)
print(name)

num_list = [1, 3, 1, 5, 3, 6, 1]
print([num for num in set(num_list)])
# n = []
# print([[num for num in num_list if num not  in n].append(num) ])

tmp = []
for num in num_list:
    if num not in tmp:
        tmp.append(num)
    else:
        continue

print(tmp)

# 14、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]？
num_list = [1, 2, 3, 4, 5]
print([x for x in list(map(lambda x: x * x, num_list)) if x > 10])

# python中生成随机整数、随机小数、0–1之间小数方法？
import random

print(random.randint(1, 10))
print(random.random())
print(random.uniform(2, 6))

# Python的浮点类
import decimal

# 随机字符串
import string

print(''.join((random.choice(string.printable)) for i in range(16)))

# <div class="nam">中国</div>
import re

s = '<div class="nam">Python</div>'
print(re.findall(r'<div class=".*">(.*?)</div>', s))

# 断言
# age = 10
# assert 0 < age < 10

# 当前日期
import time
import datetime

print(datetime.datetime.now())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
# 指定字典赋值

keys = ('info',)
print(dict.fromkeys(keys, ['Gage', '25', 'man']))

# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"？
s1 = "ajldjlajfdljfddd"
print(''.join(sorted(set(s1))))

# 用lambda函数实现两个数相乘？
mul = lambda x, y: x * y
print(mul(2, 4))

# 字典根据键从小到大排序？
info = {'name': 'Gage', 'age': 25, 'sex': 'man'}
print(sorted(info.items(), key=lambda x: x[0]))

# 获取参数
from urllib.parse import urlparse, parse_qs

s2 = "/get_feed_list?version_name=5.0.9.0&device_id=12242channel_name=google"


def spiltline(value):
    url = {'site': urlparse(value).path}
    url.update(parse_qs(urlparse(value).query))
    return url


# 统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter

s3 = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
print(Counter(s3))

import shutil

# shutil.copy()

# filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2, a)))

# 列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x for x in a if x % 2])

# a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
print(type((1,)))
print(type((1)))
print(type(("1")))

# 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
l1 = [1, 5, 7, 9]
l2 = [2, 2, 6, 8]
l1.extend(l2)
print(l1)

# 用python删除文件和用linux命令删除文件方法

# [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1, 2], [3, 4], [5, 6]]
print([j for i in a for j in i])

# [1,2,3]+[4,5,6]
print([1, 2, 3] + [4, 5, 6])

# a="hello"和b="你好"编码成bytes类型
b = "你好"
print(b'hello')
print(b.encode())

# zip()
a = [1, 2]
b = [3, 4]
print(list(zip(a, b)))

# list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]

# 保留两位小数（题目本身只有a=”%.03f”%1.3335,让计算a的结果，为了扩充保留小数的思路，提供round方法（数值，保留位数））
print(round(5 / 3, 2))

import re

print(re.findall(
    '((?:(?:[2468][048]00|[13579][26]00|[1-9]\d0[48]|[1-9]\d[2468][048]|[1-9]\d[13579][26])/(?:0?2/(?:0[1-9]|0?[1-9](?=\D)|[12]\d)))|(?:(?:[12]\d{3})/(?:(?:0?2/(?:0[1-9]|0?[1-9](?=\D)|1\d|2[0-8]))|(?:0?[3578]/(?:0[1-9]|0?[1-9](?=\D)|[12]\d|3[01]))|(?:0?[469]/(?:0[1-9]|0?[1-9](?=\D)|[12]\d|30))|(?:1[02]/(?:0[1-9]|0?[1-9](?=\D)|[12]\d|3[01]))|(?:11/(?:0[1-9]|0?[1-9](?=\D)|[12]\d|30))|(?:0?1/(?:0[1-9]|0?[1-9](?=\D)|[12]\d|3[01])))))',
    'Date：2018/03/20'))

# 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
dic = {"name": "zs", "age": 18}
dic.pop('name')
del dic['age']
print(dic)

# 对s="hello"进行反转
s="hello"
print(s[::-1])

# int("1.4")、int(1.4)的输出结果？
# print(int("1.4"))
print(int(1.4))