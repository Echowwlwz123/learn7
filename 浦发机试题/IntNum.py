# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 21:28
# @Author  : WANGWEILI
# @FileName: IntNum.py
# @Software: PyCharm
# 找出正整数中偶数，并输出相加后的数
import random


def IntNum(a):
    sum = 0
    i = 0
    while a > 0:
        i = a % 10
        if i % 2 == 0:
            sum += i
        a /= 10
        a = int(a)
    return sum


# 输入 n 和 b , 找出 1 到 n 中被 b 整除的个数.
def DvideNum(n, b):
    count = 0
    for i in range(1, n):
        if i % b == 0:
            count += 1
    return count


# 爬一个或者两个台阶，输入 1 <= n < 90 的数字为台阶数，以输入 0 作为结束标志，输出n个台阶共有多少种上楼方式.
def wawa(step):
    if step == 1 or step == 2:
        return step
    a = 1
    b = 2
    c = 0
    for i in range(3, step + 1):
        c = a + b
        a = b
        b = c
    return c


if __name__ == '__main__':
    # a = int(input("请输入正整数："))
    # print(IntNum(a))
    # print(DvideNum(10,4))
    print(wawa(5))
