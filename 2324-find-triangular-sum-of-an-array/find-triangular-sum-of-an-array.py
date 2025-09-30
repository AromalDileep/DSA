class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        # Keep reducing the array until one element remains
        for size in range(n, 1, -1):
            for i in range(size - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]
