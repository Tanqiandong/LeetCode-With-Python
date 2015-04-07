# Created by Clyde on 15/3/22.

#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        def depth(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            else:
                return max(depth(root.left), depth(root.right))+1
        return depth(root)
