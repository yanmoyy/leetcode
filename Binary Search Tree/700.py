# 700. Search in a Binary Search Tree

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return None
