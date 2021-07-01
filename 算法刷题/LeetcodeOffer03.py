# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 19:56
# @Author  : WANGWEILI
# @FileName: LeetcodeOffer03.py
# @Software: PyCharm
"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 数组中任意重复数字
        # 方法一：排序之后遍历,遇到第一个重复元素返回该元素之后结束！
        nums.sort()
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        # 方法三：原地置换（0将数组对应为哈希表）如果数组中不存在重复元素，
        # 那么应该下标与数字对应（长度为n的数组，其中数字的范围都在0到n-1范围内）
        n = len(nums)
        for i in range(n):
            if nums[i] != i:  # 如果遇到下标i与nums[i]不一样，那么就要把这个nums[i]换到它应该去的下标下面。
                if nums[i] == nums[nums[i]]:  # 如果那么下标下面已经被占了，那么就找到了重复，结束就好了！
                    return nums[i]
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


if __name__ == '__main__':
    print(Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
