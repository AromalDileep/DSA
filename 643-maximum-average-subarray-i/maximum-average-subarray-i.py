class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        running_sum = sum(nums[:k])
        avg = running_sum / k

        for i in range(k, len(nums)):
            running_sum += nums[i]
            running_sum -= nums[i-k]
            avg = max(avg, running_sum/k)
        
        return avg