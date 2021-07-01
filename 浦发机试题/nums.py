# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 20:13
# @Author  : WANGWEILI
# @FileName: nums.py
# @Software: PyCharm
# 给定一个包含 0, 1, 2, …, n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
class Solution:
    def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        nums.sort()
        print(nums)
        for item in nums:
            if item - i != 0:
                return i
            else:
                i += 1
        return i

    def numsM(nums):
        nums.sort()

        for key, value in enumerate(nums):
            print(f"key is:{key}")
            print(f"value is:{value}")
            if key != value:
                print(f"key is:{key}")
                return key
        else:
            return key + 1


if __name__ == '__main__':
    print(Solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(Solution.numsM([3, 0, 1]))
    print(Solution.numsM([3, 0, 1, 2]))
