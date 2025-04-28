from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for right in range(2, len(nums)):
            first = nums[right - 2]
            third = nums[right]
            middle = nums[right - 1]
            if (first + third) * 2 == middle:
                res += 1
        return res
