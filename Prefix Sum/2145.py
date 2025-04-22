from typing import List

# My Solution with Binary Search

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        def check(value):
            temp = value
            for i in range(n + 1):
                if temp < lower:
                    return "lower"
                if temp > upper:
                    return "upper"
                if i != n:
                    temp += differences[i]
            return "ok"
        left, right = lower, upper
        # min value of the first element
        while left <= right:
            mid = (left + right) // 2
            res = check(mid)
            if res == "upper" or res == "ok":
                right = mid - 1
            else:
                left = mid + 1

        min_value = left
    
        # max value of the first element
        left, right = lower, upper
        while left <= right:
            mid = (left + right) // 2
            res = check(mid)
            if res == "lower" or res == "ok":
                left = mid + 1
            else: 
                right = mid - 1
        max_value = left

        if check(min_value) != "ok":
            return 0
        else:
            return max_value - min_value


class Solution2:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        max_value, min_value, cur_value = 0, 0, 0
        for diff in differences:
            cur_value += diff
            max_value = max(max_value, cur_value)
            min_value = min(min_value, cur_value)
        bound1 = upper - lower
        bound2 = max_value - min_value
        res = bound1 - bound2 + 1
        if res < 0:
            return 0
        else:
            return res
