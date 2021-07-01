# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 22:03
# @Author  : WANGWEILI
# @FileName: Python实现链表.py
# @Software: PyCharm
class Node():
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, new_value):
        self._value = new_value

    def setNext(self, new_next):
        self._next = new_next


class LinkedList():
    def __init__(self):
        self._head = Node()
        self._tail = None
        self._length = 0

        # 检测是否为空
        def isEmpty(self):
            return self._head == None

        def indexOf(self):
            return self._head == None

        def search(self, value):
            current = self._head
            foundvalue = False
            while current != None and not foundvalue:
                if current.getValue() == value:
                    foundvalue = True
                else:
                    current = current.getNext()
            return foundvalue

        def add(self, value):
            newnode = Node(value, None)
            newnode.setNext(self._head)
            self._head = newnode

        def append(self, value):
            newnode = Node(value)
            if self.isEmpty():
                self._head = newnode
            else:
                current = self._head
                while current.getNext() != None:
                    current = current.getNext()
                current.setNext(newnode)
