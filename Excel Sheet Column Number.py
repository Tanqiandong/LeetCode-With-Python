# Created by Clyde on 15/3/27.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        s = s[::-1]
        sum = 0
        for idx, value in enumerate(s):
            sum += (int(value, 36)-9) * (26)**idx
        return sum
