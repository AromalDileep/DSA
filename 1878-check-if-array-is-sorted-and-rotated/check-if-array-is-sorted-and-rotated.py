class Solution:
    def check(self, nums: List[int]) -> bool:

        count = 0 
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1) % n]: # if rotated sorted array condition only satisfied once
                count += 1
            
        return count <= 1