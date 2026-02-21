class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0 

        for num in range(left, right+1):
            c = bin(num)[2:].count('1')

            if c < 2:
                continue

            for i in range(2, int(c**0.5) + 1):
                if c % i == 0:
                    break
            else:   # if for loop breaks else won't work
                res += 1

        return res