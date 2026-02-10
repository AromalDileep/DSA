class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:return 0
        nums.sort()
        min_diff = float("inf")
        l,r =0, k-1 
        while r < len(nums):
            min_diff = min(nums[r]- nums[l], min_diff)
            l += 1 
            r += 1 
        return min_diff