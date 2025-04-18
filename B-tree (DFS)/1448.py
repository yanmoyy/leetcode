# 1448. Count Good Nodes in Binary Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            if node.val >= max_val:
                count = 1
                max_val = node.val
            else:
                count = 0
            return count + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)
