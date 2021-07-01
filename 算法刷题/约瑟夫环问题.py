# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 20:26
# @Author  : WANGWEILI
# @FileName: 约瑟夫环问题.py
# @Software: PyCharm
"""
约瑟夫环问题：一圈共有N个人，开始报数，报到M的人自杀，然后重新开始报数，问最后自杀的人是谁？
内环表示人排列的环，外环表示自杀顺序；上面N=41,M=3。
输出自杀顺序，最后存活的人
"""
"""
maxNum:一共有多少个人
startNum:从哪一个人开始数
stepNum：每次报数喊几下
"""


def choiceNum(maxNum, startNum, stepNum):
    deleList = []
    plist = []
    count = 0
    for n in range(startNum, maxNum + 1):
        plist.append(n)
    while len(plist) > 1:
        count += 1
        tmp = plist.pop(0)
        if count == stepNum:
            deleList.append(tmp)
            count = 0
        else:
            plist.append(tmp)
    return {
        'lastData': plist[0],
        'delData': deleList
    }


result = choiceNum(10, 3, 3)
print('最后剩下的是第', result["lastData"], '人')
print('自杀顺序为', result["delData"])
