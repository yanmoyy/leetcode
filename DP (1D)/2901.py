from typing import List


class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        def get_dist(s1, s2):
            return sum(c1 != c2 for c1, c2 in zip(s1, s2))

        n = len(words)
        dp = [1] * n
        pre = [-1] * n

        for i in range(n):
            for j in range(i + 1, n):
                if groups[i] == groups[j]:
                    continue
                if len(words[i]) != len(words[j]):
                    continue
                if get_dist(words[i], words[j]) != 1:
                    continue
                if dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
                    pre[j] = i

        mx_len = max(dp)
        cur = dp.index(mx_len)
        ans = []
        while cur != -1:
            ans.append(words[cur])
            cur = pre[cur]

        return ans[::-1]
