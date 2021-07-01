# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 21:15
# @Author  : WANGWEILI
# @FileName: 内置函数-range.py
# @Software: PyCharm
res = range(10)
print(list(res))
"""
range()函数
功能：能够生成一个指定的数字序列
参数：
    start：开始的值，默认值为0
    stop：结束的值
    step：可选，步进，默认1
"""
# 从大到小生成列表，需要指定步进值
res = range(10, 0, -1)
res = range(-10, -20, -2)
print(list(res))

"""
zip()函数
功能：返回一个元组的迭代器，其中的第 i 个元组包含来自每个参数序列或可迭代对象的第 i 个元素。 当所输入可迭代对象中最短的一个被耗尽时，迭代器将停止迭代。 当只有一个可迭代对象参数时，它将返回一个单元组的迭代器。 不带参数时，它将返回一个空迭代器
参数：*iterables,任意个的可迭代对象
返回值：返回一个元组的迭代器
    
"""
var1 = '123'
var2 = ['a', 'b', 'c']
var3 = ('A', 'B', 'C')
res = zip(var1, var2, var3)
print(list(res))
# [('1', 'a', 'A'),
# ('2', 'b', 'B'),
# ('3', 'c', 'C')]
x = [1, 2, 3]
y = [4, 5, 6]
res = zip(x, y)
# zip() 与 * 运算符相结合可以用来拆解一个列表:
x2, y2 = zip(*zip(x, y))
print(x2, y2)
