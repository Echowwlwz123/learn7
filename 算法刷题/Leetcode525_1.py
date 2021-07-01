# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 7:25
# @Author  : WANGWEILI
# @FileName: Leetcode525_1.py
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
        dic = {0: -1}
        count = res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in dic:
                res = max(i - dic[count], res)
            else:
                dic[count] = i
        return res


if __name__ == '__main__':
    print(Solution().findMaxLength([0, 1, 0, 0, 1]))
