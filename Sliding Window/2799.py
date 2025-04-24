from collections import defaultdict
from typing import List


## Sliding Window Strategy
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        n = len(nums)
        count = defaultdict(int)
        left = 0
        res = 0
        for i in range(0, n):
            count[nums[i]] += 1
            while len(count) == k:
                res += n - i
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
        return res


#  O(n) with set
class Solution2:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        n = len(nums)
        res = 0
        for i in range(0, n):
            st = set()
            for j in range(i, n):
                st.add(nums[j])
                if len(st) == k:
                    res += 1
        return res
