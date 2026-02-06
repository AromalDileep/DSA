class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        max_window = 1
        left = 0

        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            max_window = max(max_window, right - left + 1)

        return n - max_window
