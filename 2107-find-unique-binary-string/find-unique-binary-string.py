from itertools import product

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)

        for combo in product("01", repeat=n):
            s = "".join(combo)
            if s not in nums:
                return s