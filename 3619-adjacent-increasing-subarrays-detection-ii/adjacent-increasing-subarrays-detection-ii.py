class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        prevRun, currRun = 0, 1 
        k = 0 

        for i in range(1, n): 
            if nums[i] > nums[i-1]:
                currRun += 1 
            else:
                prevRun = currRun
                currRun = 1
            
            k = max(k, currRun//2)
            k = max(k, min(currRun, prevRun))
        
        return k

