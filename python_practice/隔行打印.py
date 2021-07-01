# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 18:58
# @Author  : WANGWEILI
# @FileName: 隔行打印.py
# @Software: PyCharm
# ☆★
# 打印矩形
# 隔一列换一个
from click._compat import raw_input

num = 0
while num < 100:
    if num % 2 == 0:
        print(f'{num % 2}★', end=' ')
    else:
        print(f'{num % 2}☆', end=' ')
    # 换行
    if num % 10 == 9:
        print(' ')
    num += 1

print(' ')
# 隔一行换一个
num = 0
while num < 100:
    if num // 10 % 2 == 0:
        print(f'★', end=' ')
    else:
        print(f'☆', end=' ')
    # 换行
    if num % 10 == 9:
        print(' ')
    num += 1
