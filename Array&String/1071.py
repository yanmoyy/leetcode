# 1071. Greatest Common Divisor of Strings


class Solution:
    def getGCD(self, x, y):
        if y == 0:
            return x
        return self.getGCD(y, x % y)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd = self.getGCD(len(str1), len(str2))
        return str1[:gcd]
