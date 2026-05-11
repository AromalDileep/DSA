class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        res = []

        for num in nums:
            for i in str(num):
                res.append(int(i))
        return res
                