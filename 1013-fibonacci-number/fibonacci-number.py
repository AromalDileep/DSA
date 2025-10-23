class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = 5 ** 0.5
        phi = (1 + sqrt5) / 2 
        psi = (1 - sqrt5) / 2

        fib_n = (phi**n - psi**n) / sqrt5 
        return int(fib_n)