# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 22:07
# @Author  : WANGWEILI
# @FileName: Leetcode237.py
# @Software: PyCharm
# 删除链表中的节点
"""
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。
传入函数的唯一参数为 要被删除的节点 。
现有一个链表 -- head = [4,5,1,9]，它可以表示为:
示例 1：

输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2：
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(5)
    node4 = ListNode(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(node1.val, node2.val, node3.val, node4.val)
    print(Solution().deleteNode(node2))
    print(node1.val, node3.val, node4.val)
