class Solution:
    def countEven(self, num: int) -> int:
        
        count = 0
        for n in range(1, num + 1):
            x = n
            digit_sum = 0
            while x > 0:
                digit_sum += x % 10
                x //= 10
            
            if digit_sum % 2 == 0:
                count += 1
        return count