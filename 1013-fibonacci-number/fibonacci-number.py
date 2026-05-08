class Solution:
    def fib(self, n: int) -> int:
        phi = (1 + 5 ** 0.5 ) / 2
        psy = (1 - 5 ** 0.5) / 2 

        return int((phi**n - psy**n)//5**0.5)
    