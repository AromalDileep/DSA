# precomute since n <= 20 

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        for i in range(n):
            inv = ""
            for c in s: inv += "1" if c == "0" else "0"
            s += "1" + inv[::-1]
        return s[k-1]