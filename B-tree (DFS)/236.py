# 236. Lowest Common Ancestor of a Binary Tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        self.result = None

        def dfs(node):
            if not node:
                return 0
            count = node == p or node == q
            count += dfs(node.left)
            count += dfs(node.right)
            if count == 2 and not self.result:
                self.result = node
            return count

        dfs(root)
        return self.result
