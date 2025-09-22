class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            def findLeft():
                l, r = 0, len(nums)-1
                index = -1
                while l <= r:
                    mid = (l+r)//2
                    if nums[mid] == target:
                        index = mid
                        r = mid-1
                    elif nums[mid] < target:
                        l = mid+1
                    else:
                        r = mid-1
                return index
            
            def findRight():
                l, r = 0, len(nums)-1
                index = -1
                while l <= r:
                    mid = (l+r)//2
                    if nums[mid] == target:
                        index = mid
                        l = mid+1
                    elif nums[mid] < target:
                        l = mid+1
                    else:
                        r = mid-1
                return index
    
            return [findLeft(), findRight()]
            