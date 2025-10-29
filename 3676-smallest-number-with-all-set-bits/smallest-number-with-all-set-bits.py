class Solution:
    def smallestNumber(self, n: int) -> int:
        l = len(bin(n)[2:])
        s = "0b"
        for _ in range(l): 
            s += "1"
        return int(s, 2)