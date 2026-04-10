class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        last = defaultdict(list)
        res = float("inf")

        for i, num in enumerate(nums):
            last[num].append(i)

            if len(last[num]) >= 3:
                res = min(res, 2*(last[num][-1] - last[num][-3]))

        return res if res != float("inf") else -1            