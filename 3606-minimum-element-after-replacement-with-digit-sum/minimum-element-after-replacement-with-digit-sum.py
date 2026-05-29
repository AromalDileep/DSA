class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        smallest = float("inf")
        
        for num in nums:

            temp = 0
            val = num

            while val > 0:
                temp += val % 10
                val //= 10
            
            smallest = min(smallest, temp)
        
        return smallest