# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 8:43
# @Author  : WANGWEILI
# @FileName: 百钱买百鸡.py
# @Software: PyCharm
"""
一共有100块钱，需要买100只鸡
公鸡-3元
母鸡-1元-100只鸡
小鸡-0.5
问100元买100只鸡有多少种方法
"""
count = 0
for gj in range(0, 34):
    for mj in range(0, 101):
        xj = 100 - gj - mj
        if (gj * 3 + mj + xj * 0.5) == 100:
            count += 1
            print(f"公鸡{gj}只，母鸡{mj}只，小鸡{xj}只，共花费{gj * 3 + mj + xj * 0.5}元")
        else:
            continue
print(count)
