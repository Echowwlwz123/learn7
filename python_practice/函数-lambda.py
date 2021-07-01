# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 20:48
# @Author  : WANGWEILI
# @FileName: 函数-lambda.py
# @Software: PyCharm
def func(x, y):
    return x * y


res = func(1, 2)
print(res)

res = lambda x, y: x * y
print(res(2, 3))

res = lambda sex: "很man" if sex == '男' else "很nice"
print(res('女'))
