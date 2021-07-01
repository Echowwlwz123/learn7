# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 20:41
# @Author  : WANGWEILI
# @FileName: icopy.py
# @Software: PyCharm
users = {'a': 'inactive', 'b': 'active', 'c': 'inactive', 'd': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(f"users:{users}")
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(f"active_users:{active_users}")
print(f"users:{users}")
