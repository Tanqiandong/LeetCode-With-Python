# Created by Clyde on 15/4/5.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m<1 or n<1:
            return 0
        if m==1 or n==1:
            return 1

        dp = [[0 for col in range(n)] for row in range(m)]

        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1

        for row in range(1,m):
            for col in range(1,n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]
