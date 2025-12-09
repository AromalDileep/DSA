class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        left = Counter()
        right = Counter(nums)

        ans = 0

        for j in range(n):

            right[nums[j]] -= 1
            if right[nums[j]] == 0:
                del right[nums[j]]

            target = nums[j] * 2

        
            left_count = left.get(target, 0)

        
            right_count = right.get(target, 0)

            ans = (ans + left_count * right_count) % MOD

            # Now add nums[j] to left for future j's
            left[nums[j]] += 1

        return ans
