# Created by Clyde on 15/4/19.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i, length = 1, len(A)
        while i < length:
            if A[i]==A[i-1]:
                for j in range(i, length):
                    A[j-1]=A[j]
                length -= 1
                A = A[:-1:]
            else:
                i += 1
        print A
        return length

    def removeDuplicates2(self, A):
        pace, length = 0, len(A)
        for i in range(1, length):
            if A[i] == A[i-1]:
                pace += 1
                length -= 1
            A[i-pace] = A[i]
        A = A[:length:]
        print A
        return length

