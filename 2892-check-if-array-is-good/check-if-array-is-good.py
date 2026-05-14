class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)

        freq = [0] * n

        for num in nums:
            if num >= n:
                return False
            freq[num] += 1 
        
        print(freq)

        for i in range(1, n-2):
            if freq[i] != 1:
                return False
        
        return freq[n-1] == 2