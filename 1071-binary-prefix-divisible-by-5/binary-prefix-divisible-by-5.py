class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        res = []
        curr = 0

        for b in nums:
            curr = (curr * 2 + b) % 5
            res.append(curr == 0)
        return res