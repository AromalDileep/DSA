class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        for row in range(m):
            for col in range(n):
                if row > 0:
                    grid[row][col] += grid[row-1][col]
                if col > 0:
                    grid[row][col] += grid[row][col-1] 
                
                if row > 0 and col > 0:
                    grid[row][col] -= grid[row-1][col-1]
        count = 0 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] <= k:
                    count += 1 
        
        return count