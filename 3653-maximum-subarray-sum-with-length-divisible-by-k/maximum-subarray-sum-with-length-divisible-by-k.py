class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        
        # For each mod class, track the minimum prefix sum seen so far
        best = [float('inf')] * k
        best[0] = 0   # prefix sum at index 0
        
        ans = float('-inf')
        
        for i, num in enumerate(nums, 1):
            prefix += num
            mod = i % k
            
            # Candidate subarray ending at i
            ans = max(ans, prefix - best[mod])
            
            # Update smallest prefix sum for this mod group
            best[mod] = min(best[mod], prefix)
        
        return ans
