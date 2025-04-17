# 1768. Merge Strings Alternately


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ## boolean value to check if we are at the end of the word
        word1_ended = False
        word2_ended = False
        res = ""

        while i < len(word1) or i < len(word2):
            if not word1_ended:
                res += word1[i]
            if not word2_ended:
                res += word2[i]
            i += 1

            if i == len(word1):
                word1_ended = True
            if i == len(word2):
                word2_ended = True

        return res


### Answer

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         merged = []

#         for a, b in zip(word1, word2):
#             merged.append(a + b)

#         merged.append(word1[len(word2):])
#         merged.append(word2[len(word1):])

#         return "".join(merged)
