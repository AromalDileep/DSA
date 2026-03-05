class Solution:
    def minOperations(self, s: str) -> int:
        flip1 = 0
        flip2 = 0 

        for i in range(len(s)):

            if s[i] != str(i % 2):
                flip1 += 1

            if s[i] != str((i+1) % 2):
                flip2 += 1 

        return min(flip1, flip2) 