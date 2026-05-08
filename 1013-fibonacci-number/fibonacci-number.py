class Solution:
    def fib(self, n: int) -> int:
        phi = (1 + 5 ** 0.5 ) / 2
        psi = (1 - 5 ** 0.5) / 2 

        return round((phi**n - psi**n)//5**0.5)
    