class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)

        if total % 2 != 0: 
            return 0
        
        left = 0 
        count = 0
        for i in range(len(nums)-1):
            left += nums[i]

            if (left % 2) == ((total - left) % 2):
                count += 1 
        
        return count
