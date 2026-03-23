class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        mn = [[0]*n for _ in range(m)]
        mx = [[0]*n for _ in range(m)]
        mn[0][0], mx[0][0] = grid[0][0], grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    mn[i][j] = mn[i][j - 1] * grid[i][j]
                    mx[i][j] = mx[i][j - 1] * grid[i][j]
                elif j == 0:
                    mn[i][j] = mn[i - 1][j] * grid[i][j]
                    mx[i][j] = mx[i - 1][j] * grid[i][j]
                else:
                    a = mn[i - 1][j] * grid[i][j]
                    b = mx[i - 1][j] * grid[i][j]
                    c = mn[i][j - 1] * grid[i][j]
                    d = mx[i][j - 1] * grid[i][j]
                    mn[i][j] = min(a, b, c, d)
                    mx[i][j] = max(a, b, c, d)
            
        res = mx[-1][-1]
        return res % MOD if res >= 0 else -1