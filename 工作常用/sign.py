#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:sign.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 14:41   
@Version:1.0
'''

# 以下进行字典签名排序
sign_data = {'a': 12, 'e': 11, 'b': 77}

print(sorted(sign_data.items()))

print([(key, value) for key, value in sorted(sign_data.items())])

print(sorted(sign_data.items(), key=lambda x: x[0]))
