# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 19:00
# @Author  : WANGWEILI
# @FileName: 列表基础.py
# @Software: PyCharm
# 列表基本操作
varlist1 = [1, 2, 3]
varlist2 = ['a', 'b', 'c']
res = varlist1 + varlist2
print(res)  # [1, 2, 3, 'a', 'b', 'c']

res = varlist1 * 3
print(res)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

res = 'a' in varlist2  # True
res = varlist1[1]
res = varlist1[-3] = 'cc'
# res = varlist2[4] = 'ff'#IndexError: list assignment index out of range

varlist2.append('aa')  # ['a', 'b', 'c', 'aa']
varlist2.append(['cc', 'dd'])  # ['a', 'b', 'c', 'aa', ['cc', 'dd']]

res = len(varlist2)

del varlist2[2]  # ['a', 'b', 'aa', ['cc', 'dd']]

res = varlist2.pop()
print(res)  # ['cc', 'dd']
print(varlist2)  # ['a', 'b', 'aa']

res = varlist1 * 3  # ['cc', 2, 3, 'cc', 2, 3, 'cc', 2, 3]
print(res)

"""
1.列表[開始索引:]
2.列表[開始索引:結束索引]
3.列表[:結束索引]
4.列表[開始索引:結束索引:步進值]
5.列表[::]
6.列表[::步進值]
"""
# 列表切片
varlist = ['刘德华', '张学友', '张国荣', '黎明', '郭富城', '小沈阳', '宋小宝', '赵四', '刘能']
res = varlist[1:6:2]  # ['张学友', ' QCdz['刘德华', '张学友', '张国荣', '黎明']e黎明', '小沈阳']
res = varlist[::]  # ['刘德华', '张学友', '张国荣', '黎明', '郭富城', '小沈阳', '宋小宝', '赵四', '刘能']
res = varlist[2:]  # ['张国荣', '黎明', '郭富城', '小沈阳', '宋小宝', '赵四', '刘能']
res = varlist[:4]  # ['刘德华', '张学友', '张国荣', '黎明']
res = varlist[0:3]  # ['刘德华', '张学友', '张国荣']
res = varlist[::3]  # ['刘德华', '黎明', '宋小宝']
res = varlist[8:1:-1]  # ['刘能', '赵四', '宋小宝', '小沈阳', '郭富城', '黎明', '张国荣']
res = varlist[8:1:-2]  # ['刘能', '宋小宝', '郭富城', '张国荣']
res = varlist[::-2]  # ['刘能', '宋小宝', '郭富城', '张国荣', '刘德华']
res = varlist[5::-1]  # ['小沈阳', '郭富城', '黎明', '张国荣', '张学友', '刘德华']
res = varlist[:3:-1]  # ['刘能', '赵四', '宋小宝', '小沈阳', '郭富城']
# res = varlist[2:6]='a'#['刘德华', '张学友', 'a', '宋小宝', '赵四', '刘能']
# res = varlist[2:6]='123'#['刘德华', '张学友', '1', '2', '3', '宋小宝', '赵四', '刘能']
res = varlist[2:6] = ['a', 'b', 'c', '1', '2', '3']  # ['刘德华', '张学友', 'a', 'b', 'c', '1', '2', '3', '宋小宝', '赵四', '刘能']
del varlist[2:6:2]  # ['刘德华', '张学友', 'b', '1', '2', '3', '宋小宝', '赵四', '刘能']

print(varlist)
