#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:不可变字典.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 15:59   
@Version:1.0
'''


# to_dist
class myDict(dict):
    def __setitem__(self, key, value):
        raise TypeError("inmutabledict can not be modifyed value")

    def to_dict(self):
        return self.__setitem__()


d = myDict({1: 2, 3: 4})
l = d.to_dict()
print(l)
l[1] = 9
