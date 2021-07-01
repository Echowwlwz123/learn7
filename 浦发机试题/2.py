# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 9:38
# @Author  : WANGWEILI
# @FileName: 2.py
# @Software: PyCharm
"""
"给你一个以二进制形式表示的数字字符串，
请返回按下述规则将其减少到1 所需要的步骤数。
规则如下： 如果当前数字为偶数，则将其除以 2 。
如果当前数字为奇数，则将其加上 1 。
题目保证你总是可以按上述规则将测试用例变为 1 。
注意：数字字符串s的要求 1 <= s.length <= 500 s 由字符 '0' 或 '1' 组成。 s[0] == '1'"
"""


def nums(s):
    if len(s) >= 1 and len(s) <= 500:
        nums = int(s, 2)
        print(nums)
        if nums % 2 == 0:
            nums = nums / 2
        else:
            nums += 1
    return nums


stopword = ''
str = ''
for line in iter(input, stopword):
    str += line
print(nums(str))
