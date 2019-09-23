# -*- encoding: utf-8 -*-

# @File:count.py 
# @Author:fovegage
# @Contact:fovegage@gmail.com
# @Created Time:2019/9/2 16:05   
# @Version:1.0


from itertools import count, cycle, chain, compress, combinations, dropwhile

# for i in count(10, 5):
#     print(i)


# for i in cycle("ABC"):
#     print(i)


# 创建更节约内存的迭代器
# for i in chain("ABC"):
#     print(i)
#
# # 过滤输出  a c d
# for i in compress(['a', 'b', 'c', 'd'], (1, 0, 1, 1)):
#     print(i)
#
# # 排列组合
# for i in combinations('ABC', 2):
#     print(i)

# 条件判断
for i in dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, ]):
    print(i)

