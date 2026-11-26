class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        decrement = 10

        alice = 1
        while n >= 0:

            alice ^= 1
            n -= decrement
            decrement -= 1

        return True if alice else False

