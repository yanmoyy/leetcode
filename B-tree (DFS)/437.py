# 437. Path Sum III

from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixSum = collections.defaultdict(int)
        prefixSum[0] = 1

        def dfs(node, currentSum) -> int:
            if not node:
                return 0
            currentSum += node.val
            # if the there was a path that had the sum of currentSum - targetSum,
            # then the current path has a path that sums to targetSum
            count = prefixSum[currentSum - targetSum]
            prefixSum[currentSum] += 1
            count += dfs(node.left, currentSum) + dfs(node.right, currentSum)
            prefixSum[currentSum] -= 1

            return count

        return dfs(root, 0)
