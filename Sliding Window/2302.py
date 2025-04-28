from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, tot, res = 0, 0, 0
        for right in range(len(nums)):
            tot += nums[right]
            while tot * (right - left + 1) >= k and left <= right:
                tot -= nums[left]
                left += 1
            res += right - left + 1
        return res
