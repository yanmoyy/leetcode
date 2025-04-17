# 724. Find Pivot Index

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        pivot = -1
        right_sum = sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                pivot = i
                break
            left_sum += nums[i]
        return pivot
