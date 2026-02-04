class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n < 4:
            return False 
        
        i = 0 

        while i < n-1 and nums[i] < nums[i+1]:
            i += 1
        
        if i == 0 or i == n-1:
            return False

        j = i 

        while j < n-1 and nums[j] > nums[j+1]:
            j += 1
        
        if j == i or j == n-1:
            return False 
        
        k = j
        
        while k < n-1 and nums[k] < nums[k+1]:
            k += 1
        
        return k == n-1
        