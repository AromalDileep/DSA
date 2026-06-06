class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum, right_sum = [0] * n , [0]*n

        for i in range(1,n):
            left_sum[i] = nums[i-1] + left_sum[i-1]

        for i in range(n-2, -1,-1):
            right_sum[i] = nums[i+1] + right_sum[i+1]
        
        return [abs(left_sum[i] - right_sum[i]) for i in range(n)]