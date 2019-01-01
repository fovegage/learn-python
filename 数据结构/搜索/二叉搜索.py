# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 16:00
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 二叉搜索.py
# @Software: PyCharm

# 假设存在一个有序的列表 我们不断地取中间进行搜索

def binsearch(target, list):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == list[mid]:
            return mid
        elif target < list[mid]:
            right -= 1
        else:
            left += 1

    return -1

print(binsearch(9, [1, 2, 5, 7, 8, 9]))
