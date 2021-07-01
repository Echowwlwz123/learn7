# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 8:29
# @Author  : WANGWEILI
# @FileName: strPractice3.py
# @Software: PyCharm
from click._compat import raw_input

a = []
while 1:
    try:
        user_input = raw_input('please input a number:')
        if user_input.strip() == 'over':
            break
        else:
            a.append(int(user_input))
    except:
        print('error,try again!')
    print(f"a is ：{a}")
    max_num = max(a)
    min_num = min(a)
    max_num_index = a.index(max_num)  # 查找某个元素
    min_num_index = a.index(min_num)
    # 方法1
    a[0], a[max_num_index] = a[max_num_index], a[0]
    a[-1], a[min_num_index] = a[min_num_index], a[-1]
    print(f"转换后a is ：{a}")
