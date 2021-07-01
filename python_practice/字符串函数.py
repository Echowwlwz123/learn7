# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 20:27
# @Author  : WANGWEILI
# @FileName: 字符串函数.py
# @Software: PyCharm
# 英文字符与字符检测相关函数
varstr = 'i 我喜欢区安全lOvE you'
res = varstr.capitalize()
print(res)  # I love you

res = varstr.title()
print(res)  # I Love You

res = varstr.upper()
print(res)  # I LOVE YOU

res = varstr.lower()
print(res)  # i love you

res = varstr.swapcase()
print(res)  # I 我喜欢区安全LoVe YOU

# 字符检测
varstr = 'I LOVE YOU'
res = varstr.isupper()
print(res)  # True,False

res = varstr.islower()
print(res)  # True,False

res = varstr.istitle()
print(res)  # True,False

print('#' * 10)
varstr = '1m234'
res = varstr.isalnum()
print(res)  # True,False

varstr = 'avc'
res = varstr.isalpha()
print(res)  # True,False

varstr = 'av$##王伟c'
res = varstr.isascii()
print(res)  # True,False

varstr = '10.2'
res = varstr.isdecimal()
print(res)  # True,False

varstr = 'def'
res = varstr.isidentifier()
print(res)  # True,False

varstr = '   '
res = varstr.isspace()
print(res)  # True,False

varstr = ' a'
res = varstr.isprintable()
print(res)  # True,False

varstr = '123456'
res = varstr.isdigit()
print(res)  # True,False

varstr = '123456'
res = varstr.startswith('1', 0)
print(res)  # True,False

print('#' * 10)
varstr = '123 456'
res = varstr.endswith('456')
print(res)  # True,False

# 字符串查找与操作
print('字符串查找与操作' * 5)

vars = 'iloveyoutosimidailoveyouto'
res = 'love' in vars
print(res)
print(len(vars))

res = vars.find('you')
print(res)  # 5

res = vars.find('you', 10, 27)
print(res)  # 21

res = vars.rfind('you')
print(res)  # 21

res = vars.index('you')
print(res)  # 5

res = vars.rindex('you')
print(res)  # 21

res = vars.count('you')
print(res)  # 2

# 操作
vars = '  iloveyoutosimidailoveyouto  '
res = vars.strip(' ')
print(res)  # iloveyoutosimidailoveyouto

vars = '  iloveyoutosimidailoveyouto  '
res = vars.rstrip(' ')
print(res)  # iloveyoutosimidailoveyouto

vars = '  iloveyoutosimidailoveyouto  '
res = vars.lstrip(' ')
print(res)  # iloveyoutosimidailoveyouto

res = vars.split('you')
print(res)  # ['ilove', 'tosimidailove', 'to']

print('4444' * 8)
var1 = 'admin'
var2 = '123'
res = ':'.join([var1, var2])
print(res)  # admin:123

vars = 'user_admin_id_123'
res = vars.split('_')
print(res)  # ['user', 'admin', 'id', '123']

# 指定分割次数，从前往后
res = vars.split('_', 2)
print(res)  # ['user', 'admin', 'id_123']

# 指定分割次数，从后往前
res = vars.rsplit('_', 2)
print(res)  # ['user_admin', 'id', '123']

vars = ['user', 'admin', 'id', '123']
res = ':'.join(vars)
print(res)  # user:admin:id:123

var1 = 'uid=123&type=ab&kw=hh'
res = var1.split('&')
for i in res:
    r = i.split('=')
    print(r.pop())
# 123
# ab
# hh

vars = 'uid=123&type=ab&kw=hh'
res = vars.replace('=', '@')
print(res)  # uid@123&type@ab&kw@hh

res = vars.replace('=', '@', 1)
print(res)  # uid@123&type=ab&kw=hh

vars = 'love'
res = vars.center(10, '#')
print(res)  ####love###
res = vars.center(11, '#')
print(res)  ####love###

res = vars.ljust(11, '#')
print(res)  # love#######

res = vars.rjust(11, '#')
print(res)  #######love
