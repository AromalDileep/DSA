class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        binary = ""
        res = []

        for n in nums:
            binary += str(n)
            val = int(binary, 2)
            res.append(val % 5 == 0)
        return res