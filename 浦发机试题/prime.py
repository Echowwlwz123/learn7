# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 20:49
# @Author  : WANGWEILI
# @FileName: prime.py
# @Software: PyCharm
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
        else:
            print(n, "is a prime number")
