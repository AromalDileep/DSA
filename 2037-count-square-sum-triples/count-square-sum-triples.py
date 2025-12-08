class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        for i in range(1, n + 1):
            for j in range(i, n + 1):

                k = int(sqrt(i**2 + j**2))
                if k <= n and i**2 + j**2 == k**2:
                    count += 2
                
        return count
