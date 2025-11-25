class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        ones = 1
        count = 1
        if k % 2 == 0 or k % 5 == 0:
            return -1
 
        while True:
            if ones % k == 0:
                return count
            ones = (ones * 10 + 1) % k
            count += 1

