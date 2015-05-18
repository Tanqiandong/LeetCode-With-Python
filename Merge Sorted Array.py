# Created by Clyde on 15/5/10.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        tmp = [0 for i in range(m+n)]
        i, j, k = 0, 0, 0
        while(i<m and j<n):
            if nums1[i] <= nums2[j]:
                tmp[k] = nums1[i]
                i += 1
            else:
                tmp[k] = nums2[j]
                j += 1
            k += 1

        if i == m :
            while j < n:
                tmp[k] = nums2[j]
                j += 1
                k += 1
        elif j == n:
            while i < m:
                tmp[k] = nums1[i]
                i += 1
                k += 1

        for i in range(m + n):
            nums1[i] = tmp[i]

