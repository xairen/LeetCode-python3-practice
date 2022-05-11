class Solution:
    def reverseWords(self, s: str) -> str:
        newS = s.split(" ")
        result = []
        for i in newS:
            i = i[::-1]
            result.append(i)
        return " ".join(result)