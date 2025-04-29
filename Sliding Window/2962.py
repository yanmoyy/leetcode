from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        n = len(nums)
        cnt, l, res = 0, 0, 0
        for r in range(n):
            if nums[r] == max_num:
                cnt += 1
            while cnt >= k and l <= r:
                cnt -= nums[l] == max_num
                l += 1
            res += l
        return res
