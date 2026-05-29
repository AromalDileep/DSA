class Solution:
    def minElement(self, nums: List[int]) -> int:
    
        smallest = float("inf")

        for num in nums:
            digit_sum = 0 

            while num > 0:
                digit_sum += num % 10
                num //= 10 
            
            smallest  = min(smallest, digit_sum)
        
        return smallest