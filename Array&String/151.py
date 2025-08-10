# 151. Reveres Words in a String


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)


# Do manually like c++


class Solution2:
    def reverseWords(self, s: str) -> str:
        list = []  # word list
        tempW = ""  # temp word
        for c in s:
            if c == " ":
                if tempW != "":
                    list.append(tempW)
                    tempW = ""
            else:
                tempW += c
        if tempW != "":
            list.append(tempW)  # add the last word

        result = ""
        for i in range(len(list) - 1, -1, -1):
            result += list[i]
            if i != 0:
                result += " "
        return result
