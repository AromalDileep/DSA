class Solution:
    def smallestNumber(self, n: int) -> int:
        l = n.bit_length()
        return (1 << l) - 1