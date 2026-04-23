class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        count = defaultdict(int)
        total = defaultdict(int)
        
        # LEFT PASS
        for i, num in enumerate(nums):
            res[i] += count[num] * i - total[num]
            count[num] += 1
            total[num] += i
        
        # reset for RIGHT PASS
        count.clear()
        total.clear()
        
        # RIGHT PASS
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            res[i] += total[num] - count[num] * i
            count[num] += 1
            total[num] += i
        
        return res