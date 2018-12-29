# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 16:41
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : get_stu.py
# @Software: PyCharm

import requests

l = requests.request('get', "https://lab.gaozhe.top/random/")
print(l.json())