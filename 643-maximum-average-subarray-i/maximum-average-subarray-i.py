class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        running_sum = sum(nums[:k])
        avg = running_sum / k

        l, r = 0, k

        while r < len(nums):
            running_sum -= nums[l]
            running_sum += nums[r]

            l += 1
            r += 1
            avg = max(avg, running_sum/k)
        
        return avg
