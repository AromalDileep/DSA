class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        cost = nums[0]
        temp = nums[1:]
        temp.sort()

        cost += temp[0]+temp[1]
        return cost