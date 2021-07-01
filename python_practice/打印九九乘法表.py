# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 8:12
# @Author  : WANGWEILI
# @FileName: 打印九九乘法表.py
# @Software: PyCharm
# 打印九九乘法表
"""
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
1x4=4 2x4=8 3x4=12 4x4=16
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}x{j}={i * j}", end=" ")
    print(' ')
print("反着输出")
for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print(f"{i}x{j}={i * j}", end=" ")
    print(' ')
print("while循环")
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{i}x{j}={i * j}", end=" ")
        j += 1
    print(' ')
    i += 1
