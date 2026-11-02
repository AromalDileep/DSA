class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        
        nums.sort()
        median = nums[len(nums) // 2]
        res = 0 

        for num in nums:
            res += abs(num-median)

        return res