# 443. String Compression

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        count: int = 1
        cur: str = chars[0]
        result: str = cur
        for c in chars[1:]:
            if c == cur:
                count += 1
            else:
                if count > 1:
                    result += str(count)
                result += c
                cur = c
                count = 1

        if count > 1:
            result += str(count)

        chars[:] = list(result)

        return len(result)
