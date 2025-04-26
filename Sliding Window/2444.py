from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans, left, mini, maxi = 0, 0, -1, -1
        for i in range(len(nums)):
            num = nums[i]
            if num < minK or num > maxK:
                left = i + 1
                continue
            if num == minK:
                mini = i
            if num == maxK:
                maxi = i
            ans += max(0, min(mini, maxi) - left + 1)
        return ans
