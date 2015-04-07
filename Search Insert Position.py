# Created by Clyde on 15/3/30.
#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i in range(len(A)):
            if A[i]>=target:
                return i
        return i+1

