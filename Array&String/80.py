from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1
        cnt = 1

        def append(value):
            nonlocal j
            nums[j] = value
            j += 1

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                cnt = 1
                append(nums[i])
            else:
                if cnt < 2:
                    cnt += 1
                    append(nums[i])
        return j
