# Created by Clyde on 15/3/7.

#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:

    def singleNumber(self, A):
        result = 0

        for integer in A:
            result ^= integer

        return result

mySolution = Solution()

print mySolution.singleNumber([2,2,3,3,4])
