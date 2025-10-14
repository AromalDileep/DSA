class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        min1 = min2 = float('inf')
        for price in prices:
            if price < min1:
                min2 = min1
                min1 = price
            elif price < min2:
                min2 = price

        total = min1 + min2
        return money - total if total <= money else money 
        