# Created by Clyde on 15/4/2.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        way = [0,1,2]
        if n > 2:
            i = 3
            while i < n + 1:
                way.append(way[i-1]+way[i-2])
                i += 1
        return way[n]
