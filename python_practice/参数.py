# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 9:25
# @Author  : WANGWEILI
# @FileName: 参数.py
# @Software: PyCharm
def love(a, b, c=3, *args, name):
    print(a, b, c)
    print(args, type(args))


love(1, 2, 3, 4, 5, 6, name='admin')


def love2(a, b, c=3, *args, name, **kwargs):
    print(a, b, c)
    print(args, type(args))  # 普通收集参数，会把多余的参数收集为元祖，tuple
    print(kwargs, type(kwargs))  # 关键字收集参数，会把多余的关键字参数收集为字典，dic


love2(1, 2, 3, 4, 5, 6, name='admin', age='22', sex='ccc', ab='aa', bc='bb')
