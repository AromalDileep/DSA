class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            if counts[num] >= 3:
                indices[num].append(i)
        
        if not indices:
            return -1

        res = float("inf")

        for ids in indices.values():
            for i in range(len(ids) - 2):
                res = min(res, 2 * (ids[i+2] - ids[i]))

        return res