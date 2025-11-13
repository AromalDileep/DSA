class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        ones = 0
        res = 0

        i = 0
        while i < n:
            if s[i] == '0':
                while i < n and s[i] == '0':
                    i += 1
                res += ones
            else:
                ones += 1
                i += 1

        return res
