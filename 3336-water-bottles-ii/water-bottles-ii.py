class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            # Exchange once
            empty -= numExchange
            numBottles = 1   # get 1 new bottle
            total += 1
            empty += numBottles
            numExchange += 1  # cost increases each time

        return total
