class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)

        nums3  = nums1 + nums2
        nums3.sort()
        k = m + n
        if k % 2 == 0:
            median_index = k//2
            return float((nums3[median_index] + nums3[median_index - 1])/2)
        else:
            median_index = k//2
            return float(nums3[median_index])
            
            