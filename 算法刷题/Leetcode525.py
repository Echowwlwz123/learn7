# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 20:00
# @Author  : WANGWEILI
# @FileName: Leetcode525.py
# @Software: PyCharm
"""
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        first_ID = dict()  # key:value字典
        first_ID[0] = -1
        cnt0, cnt1 = 0, 0
        for i, x in enumerate(nums):
            cnt0 += (x == 0)
            cnt1 += (x == 1)
            d = cnt0 - cnt1
            if d in first_ID:
                res = max(res, i - first_ID[d])
            else:
                first_ID[d] = i
        return res


if __name__ == '__main__':
    print(Solution().findMaxLength([0, 1, 1, 0, 1, 0]))
