# Created by Clyde on 15/3/31.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for ele in A:
            ones = ones^ele & ~twos
            twos = twos^ele & ~ones
        return ones
