# Created by Clyde on 15/4/8.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        peak = -999999999999
        for i in range(len(num)):
            if num[i] > peak:
                peak = num[i]

        return num.index(peak)

