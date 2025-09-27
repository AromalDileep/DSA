from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Count the number of triplets that can form valid triangles.
        A triangle is valid if nums[i] + nums[j] > nums[k],
        where nums[k] is chosen as the largest side.
        """
        nums.sort()
        n = len(nums)
        count = 0

        # Fix the largest side nums[largest]
        for largest in range(n - 1, 1, -1):
            left, right = 0, largest - 1

            while left < right:
                if nums[left] + nums[right] > nums[largest]:
                    # If nums[left] + nums[right] > nums[largest],
                    # then all elements between left..(right-1) with nums[right]
                    # also satisfy the condition because the array is sorted.
                    count += right - left
                    right -= 1
                else:
                    # Otherwise, increase left to make the sum larger
                    left += 1

        return count
