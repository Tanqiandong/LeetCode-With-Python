# Created by Clyde on 15/4/19.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carry = 0
        length = len(digits)
        digits[length-1] += 1
        for i in range(length-1, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
                if i == 0:
                    digits.insert(0,1)
            else:
                carry = 0
        return digits
