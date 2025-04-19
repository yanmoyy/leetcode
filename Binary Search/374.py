# 374. Guess Number Higher or Lower


class Solution:

    def guessNumber(self, n: int) -> int:
        def guess(num: int) -> int:
            pass

        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1
        return -1
