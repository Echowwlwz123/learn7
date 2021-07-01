# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 15:27
# @Author  : WANGWEILI
# @FileName: 内置函数-高阶函数.py
# @Software: PyCharm
# sorted()
"""
功能：排序
    把可迭代数据里的元素，一个一个取出来，放到KEY这个函数中处理
    并按照函数中return的结果进行排序，返回一个新的列表
参数：
    iterable 可迭代的数据
    reverse 可选，是否反转，默认False,不反转，True 反转
    key 可选，函数，可以自定义函数，也可以是内置函数
"""
from functools import reduce

arr = [3, 7, 1, -9, 10]
# res = sorted(arr)#[-9, 1, 3, 7, 10]
# res = sorted(arr,reverse=True)#[10, 7, 3, 1, -9]
# res = sorted(arr,key=abs)#[1, 3, 7, -9, 10]
arr = [3, 7, 1, -9, 10]


def func(num):
    return num % 2


res = sorted(arr, key=func)
print(res)  # [10, 3, 7, 1, -9]
# 优化
res = sorted(arr, key=lambda x: x % 2)
print(res)  # [10, 3, 7, 1, -9]
# map()
"""
map(func,*iterable)
功能：对传入的可迭代数据中的每个元素放入到函数中进行处理，返回一个新的迭代器
参数：
    func 函数 自定义函数|内置函数
    iterables:可迭代数据
返回值：迭代器
"""
# varlist = ['1','2','3','4']
# newlist = []
# for i in varlist:
#     newlist.append(int(i))
# print(newlist)
# 案例1
varlist = ['1', '2', '3', '4']
res = map(int, varlist)
res2 = map(str, *map(res))
print(list(res), list(res2))

# 案例2 [1,2,3,4]==>[1,4,9,16]
# 方法1：
num = [1, 2, 3, 4]
newlist = []
for i in num:
    newlist.append(i ** 2)
print(newlist)

# 方法2：
num = [1, 2, 3, 4]
res = map(lambda x: x ** 2, num)
print(list(res))

# 案例3 ['a','b','c','d']==>[65,66,67,68]
varlist = ['a', 'b', 'c', 'd']
newlist = []  # 分配一个新的列表
# 先把列表中的每个元素都变成大写字符
for i in varlist:
    newlist.append(i.upper())
# 用map函数，ord（把字母转换成asci码值）
res = map(ord, newlist)
print(list(res))

# reduce()
"""
reduce(func,*iterable)
功能：
    每一次从iterable中拿出两个元素，放入到func中处理，得出一个计算结果
    然后把这个计算结果和iterable中的第三个元素，放入到func函数中继续运算
    得出的结果和之后的第四个元素，加入到func函数中进行处理，以此类推，
    直到最后一个元素参与运算
参数： 
    func : 内置函数|自定义函数
    iterable: 可迭代数据
返回值：最终的运算处理结果
注意：使用reduce函数时需要导入from functools import reduce
"""
# 案例1：[5,2,1,1]==>5211
# 方法1：
varlist = [5, 2, 1, 1]
res = ''
for i in varlist:
    print(i, type(i))
    res += str(i)
res = int(res)
print(res)

# 方法2：
varlist = [5, 2, 1, 1]
res = reduce(lambda i, j: i * 10 + j, varlist)
print(res)

# 案例2：把字符串'456'==>456
# 方法1：
varlist = '456'
res = int(varlist)
print(res)
# 方法2：
varlist = '456'
# it1 = map(int,varlist)
res = reduce(lambda x, y: x * 10 + y, map(int, varlist))
print(res)

# 方法3：不使用int函数
varlist = '456'


def func(s):
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return dic[s]


# iter1 = map(func,varlist)
res = reduce(lambda x, y: x * 10 + y, map(func, varlist))
print(res)

# filter()
"""
filter(func,iterable)
功能：过滤数据，把iterable中的每个元素拿到func函数中进行处理，
    如果函数返回True则保留这个数据，返回False则丢弃这个数据
参数：
    func :自定义函数
    iterable: 可迭代的数据
返回值：保留下来的数据组成的迭代器
"""
# 案例1:要求保留所有的偶数，丢弃所有的奇数
varlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = []
for i in varlist:
    if i % 2 == 0:
        newlist.append(i)
print(newlist)


# 方法2：
def func(n):
    if n % 2 == 0:
        return True
    else:
        return False


varlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = filter(func, varlist)
print(list(res))

# 方法3：
varlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = filter(lambda x: True if x % 2 == 0 else False, varlist)
print(list(res))
