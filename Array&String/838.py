from collections import defaultdict


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        falling = []
        result = list(dominoes)
        for i in range(n):
            if result[i] != ".":
                falling.append(i)

        while falling:
            check = defaultdict(int)

            for i in falling:
                d = result[i]
                if d == "L":
                    dx = -1
                else:
                    dx = 1
                nxt = i + dx
                if nxt >= 0 and nxt < n and result[nxt] == ".":
                    check[nxt] += dx

            falling = []
            for key in check:
                if check[key] < 0:
                    result[key] = "L"
                    falling.append(key)
                elif check[key] > 0:
                    result[key] = "R"
                    falling.append(key)

        return "".join(result)


class Solution2:
    def pushDominoes(self, dominoes: str) -> str:
        s = "L" + dominoes + "R"
        res = ""
        pre = 0
        for cur in range(1, len(s)):
            if s[cur] == ".":
                continue
            if pre > 0:
                res += s[pre]
            span = cur - pre - 1
            if s[pre] == s[cur]:
                res += s[pre] * span
            elif s[pre] == "L" and s[cur] == "R":
                res += "." * span
            else:
                res += "R" * (span // 2) + "." * (span % 2) + "L" * (span // 2)
            pre = cur
        return res
