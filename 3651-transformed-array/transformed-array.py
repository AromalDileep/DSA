class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
    
        for i, num in enumerate(nums):
            result[i] = nums[(i + num) % n]
        
        return result

