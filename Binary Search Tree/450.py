# 450. Delete Node in a BST

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Find the successor (smallest node in the right subtree)
            parent = root
            successor = root.right

            while successor.left:
                parent = successor
                successor = successor.left

            # Delete the successor from its current position
            if parent == root:
                parent.right = successor.right
            else:
                parent.left = successor.right

            # Replace the root with the successor
            successor.left = root.left
            if root.right != successor:
                successor.right = root.right

            return successor

        return root
