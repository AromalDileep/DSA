class Solution:
    def reverse(self, x: int) -> int:
        result = 0 
        sign = -1 if x < 0 else 1
        x = abs(x)

        MAX = 2 ** 31 -1 
        MIN = -2 ** 31

        while x != 0:
            digit = x % 10
            x //= 10
            
            if result > MAX // 10 or (result== MAX and digit >= MAX % 10):
                return 0 
            if result < MIN // 10 or (result == MIN and digit <= MIN % 10):
                return 0 

            result = (result * 10) + digit
        
        return sign * result