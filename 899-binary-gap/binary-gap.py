class Solution:
    def binaryGap(self, n: int) -> int:
        num = bin(n)[2:]
        res = 0
        l = 0
        
        while l < len(num):
            if num[l] == '1':
                r = l + 1
                while r < len(num) and num[r] != '1':
                    r += 1
                if r < len(num):
                    res = max(res, r - l)
                l = r
            else:
                l += 1
                
        return res