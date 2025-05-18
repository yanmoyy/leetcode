from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        j = 0
        for i in range(len(nums)):
            while j < 3 and count[j] == 0:
                j += 1
            nums[i] = j
            count[j] -= 1
        return
