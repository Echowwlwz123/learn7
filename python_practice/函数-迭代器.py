# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 20:53
# @Author  : WANGWEILI
# @FileName: 函数-迭代器.py
# @Software: PyCharm
from collections.abc import Iterable, Iterator

for i in range(10, 3, -1):
    print(i)
"""
iter()
功能：把可迭代对象，转为一个迭代器对象
参数：可迭代对象（str,list,tuple,dict,set,range....）
返回：迭代器对象
注意：迭代器一定是一个可以迭代的对象，但是可迭代对象不一定是迭代器
"""
# f4 = ['赵四','刘能','小沈阳','海参炒面']
# res = iter(f4)
# r = next(res)
# print(r)
# r = next(res)
# print(r)
# r = next(res)
# print(r)
# r = next(res)
# print(r)
# r = next(res)#超出可迭代范围，报错StopIteration
# print(r)
# 迭代器取值方案
"""
1.next()调用一次获取一次，直到数据被取完
2.list() 使用list函数直接取出迭代器中的所有数据
3. for 使用for循环遍历迭代器的数据

"""
varstr = '123456'
var = iter(varstr)
r1 = isinstance(varstr, Iterable)  # 可迭代对象
r2 = isinstance(varstr, Iterator)  # 不是一个迭代器
r3 = isinstance(var, Iterable)  # 可迭代对象
r4 = isinstance(var, Iterator)  # 是一个迭代器

print(r1, r2, r3, r4)
# 迭代器一定是一个可迭代对象，可迭代对象不一定是迭代器
