# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 8:10
# @Author  : WANGWEILI
# @FileName: strPractice.py
# @Software: PyCharm
l = input('请输入一个数组：')
z = l.strip('[').strip(']').split(',')
x = []
for i in z:
    y = int(i)
    x.append(y)
for m in x:
    for i in range(len(x)):
        if x[i] > m:
            m = x[i]
    x.remove(m)
for n in x:
    for i in range(len(x)):
        if x[i] < n:
            n = x[i]
    x.remove(n)
    x.insert(0, m)
    x.append(n)
print(x)
