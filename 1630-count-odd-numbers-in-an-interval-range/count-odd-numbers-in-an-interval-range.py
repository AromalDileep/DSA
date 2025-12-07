class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0 and high % 2 != 0: 
            return ((high+2) - low) // 2
        
        if low % 2 !=0 or high % 2 != 0:
            return ((high+1)-low) // 2
        
        return (high - low) //2
