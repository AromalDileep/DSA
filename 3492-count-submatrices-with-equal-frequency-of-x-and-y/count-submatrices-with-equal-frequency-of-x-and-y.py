class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        res = 0 

        x = [[0]*n for _ in range(m)]
        y = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 'X':
                    x[i][j] += 1
                elif grid[i][j] == 'Y':
                    y[i][j] += 1
                
                if i > 0:
                    x[i][j] += x[i-1][j]
                    y[i][j] += y[i-1][j]
                if j > 0:
                    x[i][j] += x[i][j-1]
                    y[i][j] += y[i][j-1]
                if i > 0 and j > 0:
                    x[i][j] -= x[i-1][j-1]
                    y[i][j] -= y[i-1][j-1]
                
                if x[i][j] > 0 and x[i][j] == y[i][j]:
                    res += 1
        
        return res