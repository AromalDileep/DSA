class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        highest, lowest = max(nums), min(nums)
        diff = highest - lowest
        return k * diff