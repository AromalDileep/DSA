class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        pref = [0] * len(nums)
        suf = [0] * len(nums)

        pref[0] = nums[0]
        for i in range(len(nums)):
            pref[i] = nums[i] + pref[i-1]
        
        suf[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suf[i] = nums[i] + suf[i+1]
  
        count = 0
        for i in range(len(nums)-1):
            if (pref[i] - suf[i+1]) % 2 == 0:
                count += 1 
        
        return count