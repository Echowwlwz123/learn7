# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 19:02
# @Author  : WANGWEILI
# @FileName: Leetcode283.py
# @Software: PyCharm
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
使用双指针
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针，用指针j记录列表中0的位置，i遍历列表的元素，碰到非0的元素，交换i,j
        # 时间复杂度O(n)
        # 空间复杂度O(1)，只是对原数组进行替换操作
        # j=0
        # for i in range(len(nums)):
        #     if nums[i] !=0:
        #         nums[j],nums[i]= nums[i], nums[j]
        #         j += 1
        ## 循环记录0元素的个数，并且遇到非0元素时候，将非0元素替换到0元素的位置
        # count 记录0元素的个数， i - count实际上是记录了零元素的位置。
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count += 1
        #     elif count > 0:
        #         nums[i - count], nums[i] = nums[i], 0

        # 循环遍历数组，当遇到非零元素的时候替换掉前面0元素
        # j 记录最新非零元素的位置
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1

        return nums


if __name__ == '__main__':
    print(Solution().moveZeroes([1, 2, 0, 0, 3, 8, 0]))
