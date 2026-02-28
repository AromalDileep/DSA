class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        MOD = 10**9 + 7

        for i in range(1, n+1):
            res += bin(i)[2:] 

        
        return int(res, 2) % MOD