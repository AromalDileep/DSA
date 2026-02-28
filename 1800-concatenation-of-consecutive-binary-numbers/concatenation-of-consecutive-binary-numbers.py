class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0 

        for curr in range(1, n+1):
            res = ((res << curr.bit_length()) | curr) % MOD
        
        return res

