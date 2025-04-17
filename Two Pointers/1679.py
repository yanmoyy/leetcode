# 1679 Max Number of K-Sum Pairs

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return count


## Using hashmap

from collections import defaultdict


class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0
        for num in nums:
            if k - num in count and count[k - num] > 0:
                count[k - num] -= 1
                res += 1
            else:
                count[num] += 1
        return res
