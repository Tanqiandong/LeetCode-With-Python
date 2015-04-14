# Created by Clyde on 15/4/13.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for col in range(cols)] for row in range(rows)]

        dp[0][0] = grid[0][0]
        
        for row in range(1, rows):
            dp[row][0] = dp[row-1][0] + grid[row][0]


        for col in range(1, cols):
            dp[0][col] = dp[0][col-1] + grid[0][col]
        
        for col in range(1,cols):
            for row in range(1,rows):
                dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]

        return dp[rows-1][cols-1]