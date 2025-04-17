# 1657. Determine if Two Strings Are Close

from typing import List
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        return sorted(count1.values()) == sorted(count2.values()) and set(word1) == set(
            word2
        )
