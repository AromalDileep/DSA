class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones = s.count("1")
        cont = ""

        for i in range(len(s)):
            if s[i] == "1":
                cont += "1"
            else:
                break
        return ones == len(cont)