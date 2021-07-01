# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 23:43
# @Author  : WANGWEILI
# @FileName: runnian.py
# @Software: PyCharm
# 判断从1990到2010年中的润年？并打印

def PrintRunnian():
    for i in range(1990, 2010):
        if (i % 4 == 0 and i / 100 != 0 or i % 400 == 0):
            print(f"{i}年是闰年")
    return None


# 输入几个单词，将字母变换成另外一组单词输出？如果字母是i，则变换后的字母是26+i-1
# def strI():


if __name__ == '__main__':
    print(PrintRunnian())
