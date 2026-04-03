class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)

        s_counts = sorted(counts.items(), key=lambda x: x[1])
        s_counts = s_counts[::-1]

        res = []
        
        for i in range(k):
            key, val = s_counts[i]
            res.append(key)

        return res
