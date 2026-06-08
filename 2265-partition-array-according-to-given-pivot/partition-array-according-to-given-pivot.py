class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right, p = [], [], []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                p.append(num)
        return left + p + right