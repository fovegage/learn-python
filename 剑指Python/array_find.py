#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:array_find.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 18:26   
@Version:1.0
'''

"""
Q: 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
"""

a = [[1, 2, 3], [4, 5, 6]]


# print(a[0][1])

def find(array, target):
    if array is None:
        return False
    row = len(array)
    column = len(array[0])
    print("数列为{}行{}列的数组，共{}个元素".format(row, column, row * column))
    for r in range(row):
        for c in range(column):
            print(r, c)
            if a[r][c] == target:

                print('{}存在'.format(target))
    print('{}不存在'.format(target))


find(a, 9)
