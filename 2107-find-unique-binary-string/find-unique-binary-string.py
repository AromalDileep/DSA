from itertools import product
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        bins = ["0", "1"]

        combos = product(bins, repeat=n)
        combos = list(map("".join, combos))

        for num in combos:
            if num not in nums:
                return num