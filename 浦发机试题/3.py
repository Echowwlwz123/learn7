# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 9:49
# @Author  : WANGWEILI
# @FileName: 3.py
# @Software: PyCharm
"""
输入一个字符串s，只能包括英文括号( 和 )，且左右括号匹配。回车符结束输入。

字符串s长度：2<=s.length()<=50
"""
SYMBOLS = {'}': '{', ']': '[', ')': '(', '>': '<'}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()


def check(s):
    count = 0
    arr = []
    for c in s:
        if c in SYMBOLS_L:
            # 左符号入栈
            arr.append(c)
        elif c in SYMBOLS_R:
            # 右符号要么出栈，要么匹配失败
            if arr and arr[-1] == SYMBOLS[c]:
                arr.pop()
                count += 1
            else:
                return False

    return count


stopword = ''
str = ''
for line in iter(input, stopword):
    str += line
print(check(str))
