class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7 

        if len(s) == 1:
            return 0 if s == '0' else 1 

        res = 0
        i = 0 

        while i < len(s):
            length = 0 
            while i < len(s) and s[i] == '1':
                length += 1
                i += 1 
            res += (length * (length +1)) // 2
            i += 1
        return res % MOD