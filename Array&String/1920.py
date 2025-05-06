from typing import List


class Solution:
    # O(1) space complexity
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += (nums[nums[i]] & 1023) << 10
        for i in range(n):
            nums[i] >>= 10
        return nums


class Solution2:
    # O(n) space complexity
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
