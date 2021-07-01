# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 21:17
# @Author  : WANGWEILI
# @FileName: 斐波那契数列.py
# @Software: PyCharm
"""
0,1,1,2,3,5,8,13....
第0项如果是0，第一项是1，第二项是1，
之后的第三项开始，每一项都是前面两个数的和
"""
num = 0
while num <= 100:
    num = int(input('请输入需要计算几项？'))
    n1 = 0
    n2 = 1
    count = 2
    if num <= 0:
        print('请输入一个正整数')
    elif num == 1:
        print(f'斐波那契数列：{n1}')
    else:
        print(f'斐波那契数列：{n1},{n2}', end=',')
        while count < num:
            n3 = n1 + n2
            print(n3, end=',')
            n1, n2 = n2, n3
            count += 1
