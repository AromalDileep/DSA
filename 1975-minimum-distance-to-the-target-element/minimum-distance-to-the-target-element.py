class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        for d in range(len(nums)):
            if start - d >= 0 and nums[start - d] == target:
                return d
            if start + d < len(nums) and nums[start + d] == target:
                return d