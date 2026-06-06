class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        res = []

        for num in nums:
            total -= num
            res.append(abs(left_sum - total))
            left_sum += num
        
        return res