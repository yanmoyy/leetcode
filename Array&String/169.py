from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        res, majority = 0, 0
        for n in nums:
            hash[n] += 1
            if hash[n] > majority:
                res = n
                majority = hash[n]

        return res


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        res, majority = 0, 0

        for n in nums:
            if majority == 0:
                res = n

            majority += 1 if n == res else -1

        return res
