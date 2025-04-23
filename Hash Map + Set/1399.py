import collections


class Solution:
    def countLargestGroup(self, n: int) -> int:
        nums = collections.defaultdict(int)
        for i in range(1, n + 1):
            temp = str(i)
            sum = 0
            for char in temp:
                sum += int(char)
            nums[sum] += 1
        max_value = max(nums.values())
        cnt = 0
        for key in nums:
            if nums[key] == max_value:
                cnt += 1
        return cnt


## The Algorithms is same, but the code can be better.


class Solution2:
    def countLargestGroup(self, n: int) -> int:
        hashMap = collections.Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count
