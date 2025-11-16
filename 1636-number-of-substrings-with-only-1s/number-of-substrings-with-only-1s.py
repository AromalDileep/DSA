class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7 
        res = 0
        count = 0

        for ch in s:
            if ch == '1':
                count += 1
                res += count   #(works same as (n * (n+1)) // 2)
            else:
                count = 0

        return res % MOD
