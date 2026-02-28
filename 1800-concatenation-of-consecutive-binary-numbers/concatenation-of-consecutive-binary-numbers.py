class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0 

        for curr in range(1, n+1):
            res <<= curr.bit_length()
            res = (res | curr) % MOD
        
        return res

