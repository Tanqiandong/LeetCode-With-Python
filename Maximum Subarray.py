# Created by Clyde on 15/3/31.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxSum = -65536
        curSum = 0
        for i in A:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(maxSum, curSum)
        return maxSum
