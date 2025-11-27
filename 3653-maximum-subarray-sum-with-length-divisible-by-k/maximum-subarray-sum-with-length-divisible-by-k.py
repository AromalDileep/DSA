
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = [float("inf")] * k
        prefix[0] = 0 
        res = float("-inf")
        total = 0 

        for i, n in enumerate(nums):
            total += n
            length = i + 1
            prefix_index = length % k
            res = max(res, total-prefix[prefix_index])
            prefix[prefix_index] = min(prefix[prefix_index], total)

        return res 