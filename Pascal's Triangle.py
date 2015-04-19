# Created by Clyde on 15/4/19.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        source = [0 for i in range(numRows)]
        triangle = [source[:i+1:] for i in range(numRows)]

        triangle[0][0] = 1
        for i in range(1, numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    triangle[i][j] = 1
                else:
                    triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
        return triangle
