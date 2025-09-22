class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums)-1
        while start_index <= end_index:
            mid = (end_index + start_index) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end_index = mid -1
            else:
                start_index = mid + 1
        return start_index
        # binary search algorithm
        