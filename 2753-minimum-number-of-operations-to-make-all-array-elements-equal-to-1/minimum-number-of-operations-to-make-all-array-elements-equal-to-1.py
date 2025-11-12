class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones > 0:
            return len(nums) - ones

        n = len(nums)
        min_len = float('inf')

        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        return (min_len - 1 + n - 1) if min_len != float('inf') else -1
