from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        O(1) space capacity
        """
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        O(n), O(n)
        """
        n = len(nums)
        rotated = [0] * n
        for i in range(n):
            rotated[(i + k) % n] = nums[i]

        nums[:] = rotated
