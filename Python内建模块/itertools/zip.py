# -*- encoding: utf-8 -*-

# @File:zip.py 
# @Author:fovegage
# @Contact:fovegage@gmail.com
# @Created Time:2019/9/2 16:36   
# @Version:1.0

from itertools import zip_longest

d = {'A': 1, 'B': 2}.items()
# ("ABCD"), (1, 2, 3, 4)
for i in zip_longest(("ABCDE"), (1, 2, 3, 4), fillvalue=0):
    print(i)
