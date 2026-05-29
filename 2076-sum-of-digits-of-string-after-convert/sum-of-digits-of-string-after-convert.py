class Solution:
    def getLucky(self, s: str, k: int) -> int:

        num = ""

        for ch in s:
           num += str(ord(ch) - ord('a') + 1) 

        for _ in range(k):
            digit_sum = 0

            for digit in num:
                digit_sum += int(digit)
            
            num = str(digit_sum)
        
        return int(num)