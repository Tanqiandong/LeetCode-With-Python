# Created by Clyde on 15/4/3.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        merge = ListNode(0)

        if l1.val < l2.val:
            merge = l1
            merge.next = self.mergeTwoLists(l1.next, l2)

        else:
            merge = l2
            merge.next = self.mergeTwoLists(l1, l2.next)
        return merge

