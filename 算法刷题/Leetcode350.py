# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 22:54
# @Author  : WANGWEILI
# @FileName: Leetcode350.py
# @Software: PyCharm
"""
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

"""
from typing import List, Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list((Counter(nums1) & Counter(nums2]).elements())
        # return [i for i in (Counter[nums1] & Counter[nums2]).elements()]

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i = 0
        j = 0
        output = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                output.append(nums1[i])
                i += 1
                j += 1
        return output
