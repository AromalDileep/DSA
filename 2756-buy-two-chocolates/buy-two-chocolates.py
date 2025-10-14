class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort() 
        temp = money
        for i in range(2): 
            temp -= prices[i]
        
        if temp < 0: 
            return money
        else:
            return temp