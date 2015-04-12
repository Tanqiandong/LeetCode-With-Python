# Created by Clyde on 15/4/12.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @return an integer
    def maxArea(self, height):
        i, j = 0, len(height)-1
        maxContainer = 0

        print height[i],height[j]
        while i != j:
            if height[i] <= height[j]:
                if flag is True and height[i] <= height[i-1] + 1:
                    pass
                else:
                    maxContainer = max(maxContainer, height[i]*abs(i-j))
                    flag = True
                i += 1
            else:
                if flag is False and height[j-1] <= height[j] + 1:
                    pass
                else:
                    maxContainer = max(maxContainer, height[j]*abs(i-j))
                    flag = False
                j -= 1
        return maxContainer
