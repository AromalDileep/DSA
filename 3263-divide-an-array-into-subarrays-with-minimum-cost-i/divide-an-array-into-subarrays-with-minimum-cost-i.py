class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_min = float('inf')
        second_min = float('inf')

        for x in nums[1:]:
            if x < first_min:
                second_min = first_min
                first_min = x
            elif x < second_min:
                second_min = x

        return nums[0] + first_min + second_min
