class Solution:
    def largestOddNumber(self, num: str) -> str:
        l = len(num)

        i = 0
        for n in range(l-1 , -1, -1): 
            if  int(num[n]) % 2 == 1: 
                i = n
                return num[:i+1]
        return ""