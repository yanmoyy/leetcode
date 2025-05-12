from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ans = set()
        for i1 in range(n):
            if digits[i1] == 0:
                continue
            num = 100 * digits[i1]
            for i2 in range(n):
                if i1 == i2:
                    continue
                num += 10 * digits[i2]
                for i3 in range(n):
                    if i1 == i3 or i2 == i3:
                        continue
                    if digits[i3] % 2 == 0:
                        num += digits[i3]
                        ans.add(num)
                        num -= digits[i3]
                num -= 10 * digits[i2]
        return sorted(list(ans))


class Solution2:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        mpp = [0] * 10
        for d in digits:
            mpp[d] += 1
        res = []
        for i in range(1, 10):
            if mpp[i] == 0:
                continue
            mpp[i] -= 1
            for j in range(10):
                if mpp[j] == 0:
                    mpp[j] -= 1
                for k in range(0, 10, 2):
                    if mpp[k] == 0:
                        continue
                    res.append(i * 100 + j * 10 + k)
                mpp[j] += 1
            mpp[i] += 1
        return res
