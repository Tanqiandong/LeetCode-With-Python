# Created by Clyde on 15/4/1.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        i = 0
        while i < len(num)-1:
            if num[i] != num[i+1]:
                num.pop(i+1)
                num.pop(i)
                if i > 0:
                    i -= 1
            else:
                i += 1

        return num[0]