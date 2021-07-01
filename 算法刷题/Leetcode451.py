# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 22:35
# @Author  : WANGWEILI
# @FileName: Leetcode451.py
# @Software: PyCharm
# Leetcode451-根据字符出现频率排序
# 根据题目的词频进行排序，然后再从大到小根据字符以及字符的个数组合成新的字符串。
"""
输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
简单介绍一下 Counter。
它是一个用来统计出现次数的类，在 collections 包里。
Counter(s) 就可以返回一个类似字典的结构，键是s中的项，值是这个项出现的次数。
对于字符串，就是每个字符和它出现的次数。
Counter类有一个函数，叫most_common(int n)，可以返回最常出现的几项，如果不加参数，就全部返回，相当于按照出现次数从大到小输出。
输出的格式形如 [('s',4),('a',3)]。
即字符s出现4次，a出现3次
思路
将字符串使用Counter处理一下。
按照most_common()按照出现次数将它们返回。
然后将字符乘以它们的出现次数会输出n次个该字符。
比如：字符s出现4次，a出现3次
输出ssssaaa
再利用字符串的join()函数将它们通通连接起来。

"""
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([c * freq for c, freq in Counter(s).most_common()])


if __name__ == '__main__':
    print(Solution().frequencySort("tree"))
