# 1493. Longest Subarray of 1's After Deleting One Element

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, count, res = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            res = max(res, right - left)
        return res if count <= 1 else res - 1
