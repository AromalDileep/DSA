class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_counter = Counter(nums)
        max_freq = max(freq_counter.values())
        total = sum(freq for freq in freq_counter.values() if freq == max_freq)
        return total
