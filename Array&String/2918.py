from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_s1 = sum(nums1)
        sum_s2 = sum(nums2)
        zero_s1 = len(list(filter(lambda x: x == 0, nums1)))
        zero_s2 = len(list(filter(lambda x: x == 0, nums2)))
        min_s1 = sum_s1 + zero_s1
        min_s2 = sum_s2 + zero_s2
        if min_s1 > min_s2:
            if zero_s2 == 0:
                return -1
            return min_s1
        if min_s1 < min_s2:
            if zero_s1 == 0:
                return -1
            return min_s2
        return min_s1
