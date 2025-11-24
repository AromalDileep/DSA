class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        res = []
        curr = 0

        for b in nums:
            curr = curr * 2 + b
            res.append(curr % 5 == 0)
        return res