# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 23:31
# @Author  : WANGWEILI
# @FileName: suhsu2.py
# @Software: PyCharm
while True:
    num = int(input('请输入一个数：'))
    for i in range(2, num):  # 判断在num之前的数能不能把num整除
        if (num % i == 0):
            print('%d不为素数' % num)
            break
        else:
            print('%d为素数' % num)
            break
