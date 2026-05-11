class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for n in range(1, num+1):
            temp = n 
            digit_sum = sum(int(x) for x in str(temp))
            if digit_sum % 2 == 0:
                count += 1
        
        return count