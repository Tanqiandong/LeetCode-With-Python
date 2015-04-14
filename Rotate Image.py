# Created by Clyde on 15/4/14.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        for row in range(int(n/2)):
            for col in range(row, n-row-1):
                    tmp = matrix[row][col]
                    matrix[row][col]=matrix[n-col-1][row]
                    matrix[n-col-1][row]=matrix[n-row-1][n-col-1]
                    matrix[n-row-1][n-col-1]=matrix[col][n-row-1]
                    matrix[col][n-row-1]=tmp



