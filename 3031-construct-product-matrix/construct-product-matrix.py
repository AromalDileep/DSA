class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        m, n = len(grid), len(grid[0])
        
        size = m * n
        flat = [0] * size
        
        idx = 0
        for i in range(m):
            for j in range(n):
                flat[idx] = grid[i][j]
                idx += 1
        
        # Prefix
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * flat[i-1]) % MOD
        
        # Suffix
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * flat[i+1]) % MOD
        
        
        # Build result
        res = [[0]*n for _ in range(m)]
        idx = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = (prefix[idx] * suffix[idx]) % MOD
                idx += 1
        
        return res