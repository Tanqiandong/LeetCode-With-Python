# Created by Clyde on 15/4/2.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        pointer = head
        if head is None:
            return head
        while pointer.next is not None:
            if pointer.next.val == pointer.val:
                if pointer.next.next is None:
                    pointer.next = None
                else:
                    pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head
