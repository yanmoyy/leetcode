# 162. Find Peak Element

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, float("-inf"))
        nums.append(float("-inf"))

        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1


class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if mid + 1 == n or nums[mid] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left
