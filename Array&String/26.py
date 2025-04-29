from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        number_set = set()
        new_list = []
        for num in nums:
            if num not in number_set:
                number_set.add(num)
                new_list.append(num)

        nums[:] = new_list
        return len(nums)


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
