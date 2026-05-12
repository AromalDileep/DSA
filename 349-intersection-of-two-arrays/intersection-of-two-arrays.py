class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums2.sort()

        def binary_search(arr, target):
            left, right = 0, len(arr)-1

            while left <= right:
                mid = (left + right) // 2 
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        res = set()
        
        for num in nums1:
            if num not in res:
                if binary_search(nums2, num):
                    res.add(num)
        return list(res)