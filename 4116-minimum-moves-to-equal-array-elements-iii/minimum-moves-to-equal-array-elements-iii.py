class Solution:
    def minMoves(self, nums: List[int]) -> int:
        biggest = max(nums)
        res = 0 

        for num in nums:
            res += abs(num - biggest)
        
        return res