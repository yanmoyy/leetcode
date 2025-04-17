# 1456. Maximum Number of Vowels in a Substring of Given Length

from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0
        ## Initialize the count of vowels in the first k characters
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        ## Slide the window one character at a time
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        return max_count
