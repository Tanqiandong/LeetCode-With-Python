# Created by Clyde on 15/4/15.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0,nums.pop())


