class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 2**32-1
        mask_int = 2**31-1

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        return a if a <= mask_int else ~(a ^ mask)