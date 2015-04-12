# Created by Clyde on 15/4/12.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, length = 0, len(A)
        while i < length:
            if A[i] == elem:
                A.pop(i)
                length -= 1
            else:
                i += 1
        return length

mySolution =  Solution()
print mySolution.removeElement([3,3,3,3,3,3,3,3],3)
