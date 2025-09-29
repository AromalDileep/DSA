class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            # If less than 3 vertices, can't form a triangle
            if j < i + 2:
                return 0
            
            res = float('inf')
            # Try every possible middle vertex k
            for k in range(i+1, j):
                res = min(
                    res,
                    values[i] * values[k] * values[j] + dp(i, k) + dp(k, j)
                )
            return res 
        
        return dp(0, len(values)-1)
