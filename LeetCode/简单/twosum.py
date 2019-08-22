#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:twosum.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/21 11:05   
@Version:1.0
'''

"""
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arrayLength = len(nums)
        for x in range(arrayLength):
            for y in range(x + 1, arrayLength):
                if nums[x] + nums[y] == target:
                    return x, y


s = Solution()
print(list(s.twoSum([1, 2, 3, 4, 5, 6], 11)))
