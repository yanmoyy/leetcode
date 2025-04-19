# 2563. Count the Number of Fair Paris

from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def lower_bound(nums: List[int], start: int, target: int) -> int:
            left, right = start, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def upper_bound(nums: List[int], start: int, target: int) -> int:
            left, right = start, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right + 1

        nums.sort()
        res = 0
        for i in range(len(nums)):
            idx1 = lower_bound(nums, i + 1, lower - nums[i])
            idx2 = upper_bound(nums, i + 1, upper - nums[i])
            res += idx2 - idx1
        return res
