class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        max_count = 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]-1:
                count +=1
                max_count = max(count, max_count)
            else:
                count = 1
        
        return max_count