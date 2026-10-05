class Solution:
    def reverse(self, x: int) -> int:

        MIN_INT, MAX_INT = -2**31, 2**31-1

        sign = -1 if x < 0 else 1
        res = 0 

        x = abs(x)
        
        for i in range(len(str(x))):
            num = x % 10
            x //= 10
            res = (res * 10) + num
        
        if res < MIN_INT or res > MAX_INT:
            return 0
        
        return res *sign