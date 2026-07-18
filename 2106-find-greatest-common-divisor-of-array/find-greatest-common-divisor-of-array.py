class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = nums[0]
        largest = nums[0]

        for num in nums:
            if num < smallest:
                smallest = num
            elif num > largest:
                largest = num 
                
        while largest:
            smallest, largest = largest , smallest % largest
        
        return smallest
