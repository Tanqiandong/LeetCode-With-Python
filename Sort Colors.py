# Created by Clyde on 15/4/7.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        start = 0
        end = len(A)-1
        i = 0
        while i <= end:
            try:
                while A[start] == 0:
                    start += 1
                    i = start

                while A[end] == 2:
                    end -= 1
            except:
                return A

            if i > end:
                return A

            if A[i] == 0:
                A[start],A[i] = A[i],A[start]
                start += 1
            if A[i] == 2:
                A[end],A[i] = A[i],A[end]
                end -= 1
            if A[i] == 1:
                i += 1

        return A
    def sortColors2(self, A):
        i = 0
        while i < len(A):
            if A[i]==0:
                A.insert(0, A.pop(i))
            if A[i]==2:
                A.append(A.pop(i))
            i += 1
        return A

mySolution = Solution()
print mySolution.sortColors2([0])

