class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0]* (n-k+1) for _ in range(m-k+1)]


        for i in range(m):
            for j in range(n):
                if i + k <= m and j + k <= n:
                    curr  = set()
                    for ii in range(i, i+k):
                        for jj in range(j, j+k):
                            curr.add(grid[ii][jj])
                   
                    if len(curr) == 1:
                        res[i][j] = 0 
                    else:
                        mn = float("inf")
                        s = sorted(curr)
                        for index, val in enumerate(s):
                            if index == 0: continue
                            mn = min(mn, val - s[index-1])
                        res[i][j] = mn
        return res
