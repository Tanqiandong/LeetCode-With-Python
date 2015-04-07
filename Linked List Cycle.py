# Created by Clyde on 15/3/30.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        n1 = head
        n2 = head.next
        while n1 != n2:
            try:
                n2 = n2.next.next
            except:
                return False
            n1 = n1.next
        return True

