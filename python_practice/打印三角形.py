# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 20:05
# @Author  : WANGWEILI
# @FileName: 打印三角形.py
# @Software: PyCharm
# 打印三角形

# num = int(input("请输入想输入的三角形的高度数字"))
# for i in range(0,num):
#         print("*"*(i))
# print(' ')
#
# for i in range(num-1,0,-1):
#         print(" "*(num-1-i)+"★"*(2*i+1))
# print(' ')

rows = int(input('输入列数： '))
i = j = k = 1  # 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
# 等腰直角三角形1
print("等腰直角三角形1")
for i in range(0, rows):
    for k in range(0, rows - i):
        print(" * ", end=' ')
    print(' ')

# 打印实心等边三角形
print("实心等边三角形")
for i in range(0, rows):
    for k in range(0, rows - i):
        print(" ", end=' ')
    for j in range(0, i):
        print(" * ", end=' ')
    print(' ')
for i in range(0, rows):
    for k in range(0, i):
        print(" ", end=' ')
    for j in range(0, rows - i):
        print(" * ", end=' ')
    print(' ')
