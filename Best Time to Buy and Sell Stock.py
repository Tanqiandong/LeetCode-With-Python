# Created by Clyde on 15/4/12.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        minPrices, maxProfit = prices[0], 0

        for price in prices:
            maxProfit = max(maxProfit, price - minPrices)
            minPrices = min(price, minPrices)
        return maxProfit
