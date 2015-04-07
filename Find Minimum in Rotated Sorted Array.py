# Created by Clyde on 15/4/2.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num)==1:
            return num[0]
        for i in range(len(num)-1):
            if num[i]>num[i+1]:
                return num[i+1]
        return num[0]
