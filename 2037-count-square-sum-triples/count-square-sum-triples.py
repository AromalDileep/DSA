class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        for i in range(1, n + 1):
            for j in range(i, n + 1):

                k = int((i*i + j*j)**0.5)
                if k <= n and i*i +j*j == k*k:
                    count += 2
        
        return count