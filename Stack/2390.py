# 2390. Removing Stars From a String

from typing import List


class Solution:
    def removeStars(slef, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
