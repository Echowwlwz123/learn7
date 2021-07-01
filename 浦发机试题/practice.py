# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 9:13
# @Author  : WANGWEILI
# @FileName: practice.py
# @Software: PyCharm
# 给你一个整数数组nums。请创建一个整数数组result，它跟nums 长度相同，且result[i]等于nums[i]与数组中所有其它元素差的绝对值之和。
# 换句话说，result[i]=sum(|nums[i]-nums[j]|) ，其中0 <= j < nums.length 且j != i
"""
输入数组和对应数组长度：长度：3，数组：nums = [2,3,5]
输出：[4,3,5]

解释：假设数组下标从 0 开始，那么

result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4，

result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3，
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5。
"""


def _sum(arr, n):
    return (sum(arr))


nums = [12, 3, 4, 15]
n = len(nums)
for i in range(n):
    for j in range(i, n - 1):
        did = abs(nums[i] - nums[j])
        print(did)
        result = _sum(did, n)
    print(f"result:{result}")
