# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 23:27
# @Author  : WANGWEILI
# @FileName: sushu.py
# @Software: PyCharm
count = 0
while count < 10:
    x = int(input("请输入一个数:"))
    if x < 2:
        print("非素数")
        count += 1
        continue
    if x == 2:
        print("素数")
        count += 1
        continue
    for i in range(2, x):  # 判断在num之前的数能不能把num整除
        if (x % i == 0):
            print('%d不为素数' % x)
            count += 1
            break
        else:
            print('%d为素数' % x)
            count += 1
            break
