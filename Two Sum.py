# Created by Clyde on 15/5/18.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, num, target):
        process={}
        for index in range(len(num)):
            if target-num[index] in process:
                return [process[target-num[index]]+1,index+1]
            process[num[index]] = index

