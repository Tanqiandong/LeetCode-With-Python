# Created by Clyde on 15/3/22.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
  # @param prices, a list of integer
  # @return an integer
  def maxProfit(self, prices):
    ans = 0
    for i in range(0,len(prices)-1):
      if (prices[i+1]-prices[i]>0):
        ans = ans + prices[i+1]-prices[i]
    return ans

