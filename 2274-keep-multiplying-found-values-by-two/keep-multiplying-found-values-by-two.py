class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        
        for i, num in enumerate(nums):
            if nums[i] == original:
                nums[i] *= 2 
                original *= 2
        return original