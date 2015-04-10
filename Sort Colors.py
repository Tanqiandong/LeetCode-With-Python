# Created by Clyde on 15/4/7.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i = 0
        for j in range(len(A)):
            if A[i] == 0:
                A.insert(0, A.pop(i))
            elif A[i] == 2:
                A.append(A.pop(i))
                i -= 1
            i += 1
