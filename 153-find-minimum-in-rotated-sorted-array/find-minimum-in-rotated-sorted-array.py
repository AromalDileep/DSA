class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                return nums[i]
        
        return nums[0]