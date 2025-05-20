from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c = nums
        if a + b > c:
            if a == b and b == c and c == a:
                return "equilateral"
            if a == b or b == c or c == a:
                return "isosceles"
            if a != b and b != c and c != a:
                return "scalene"
        return "none"
