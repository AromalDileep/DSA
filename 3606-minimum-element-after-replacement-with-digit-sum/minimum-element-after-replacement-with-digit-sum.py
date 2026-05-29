class Solution:
    def minElement(self, nums: List[int]) -> int:
    
        smallest = float("inf")

        for num in nums:
            val = num
            total = 0 

            while val > 0:
                total += val % 10
                val //= 10 
            
            smallest  = min(smallest, total)
        
        return smallest