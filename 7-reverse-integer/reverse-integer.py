class Solution:
    def reverse(self, x: int) -> int:

        MIN_INT, MAX_INT = -2**31, 2**31-1
        
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0
        for i in range(len(str(x))):
            num = x % 10
            res = res * 10 + num
            x = x // 10
        
        ans = res * sign
        if ans < MIN_INT or ans > MAX_INT:
            return 0
        
        return ans