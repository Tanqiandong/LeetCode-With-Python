# Created by Clyde on 15/4/15.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for i in range(n)]
        row, col, num = 0, 0, 1
        while num <= n**2:
            # right
            while col < n and matrix[row][col] == 0:
                matrix[row][col] = num
                col += 1
                num += 1

            col -= 1
            row += 1

            # down
            while row < n and matrix[row][col] == 0:
                matrix[row][col] = num
                row += 1
                num += 1

            row -= 1
            col -= 1

            # left
            while col >= 0 and matrix[row][col] == 0:
                matrix[row][col] = num
                col -= 1
                num += 1

            col += 1
            row -= 1

            # up
            while matrix[row][col] == 0:
                matrix[row][col] = num
                row -= 1
                num += 1
            row += 1
            col += 1

            
        return matrix
