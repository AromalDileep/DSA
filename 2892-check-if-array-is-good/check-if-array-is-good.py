class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)

        if nums.count(n-1) != 2:
            return False
        
        nums.sort()

        count = 1
        
        for i in range(n-1):
            if nums[i] != count:
                return False
            count += 1


        return True