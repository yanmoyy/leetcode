# 1372. Longest ZigZag Path in a Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node, direction, count) -> int:
            if not node:
                return count

            if direction == "left":
                return max(
                    dfs(node.right, "right", count + 1), dfs(node.left, "left", 0)
                )
            else:
                return max(
                    dfs(node.left, "left", count + 1), dfs(node.right, "right", 0)
                )

        return max(dfs(root.left, "left", 0), dfs(root.right, "right", 0))


class Solution2:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_count = 0

        def dfs(node, left, right):
            if not node:
                return
            self.max_count = max(self.max_count, left, right)
            dfs(node.left, right + 1, 0)
            dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.max_count
