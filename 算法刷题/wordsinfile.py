# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 22:12
# @Author  : WANGWEILI
# @FileName: wordsinfile.py
# @Software: PyCharm
"""
举个计数的例子，需要统计一个文件中，每个单词出现的次数。实现方法如下

"""
# 普通青年
from collections import defaultdict, Counter

d = {}
with open('/etc/passwd') as f:
    for line in f:
        for word in line.strip().split(':'):
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

# 文艺青年
d = defaultdict(int)
# defaultdict的作用是在于，
# 当字典里的key不存在但被查找时，
# 返回的不是keyError而是一个默认值，
# 这个factory_function可以是list、set、str等等，
# 作用是当key不存在时，返回的是工厂函数的默认值，
# 比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0，

with open('/etc/passwd') as f:
    for line in f:
        for word in line.strip().split(':'):
            d[word] += 1

# 棒棒的青年
# sum(c.values())  # 所有计数的总数
# c.clear()  # 重置Counter对象，注意不是删除
# list(c)  # 将c中的键转为列表
# set(c)  # 将c中的键转为set
# dict(c)  # 将c中的键值对转为字典
# c.items()  # 转为(elem, cnt)格式的列表
# Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
# c.most_common()[:-n:-1]  # 取出计数最少的n-1个元素
# c += Counter()  # 移除0和负值
word_counts = Counter()
with open('/etc/passwd') as f:
    for line in f:
        print(line)
word_counts.update(line.strip().split(':'))
