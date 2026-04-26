class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r,c):
            visited[r][c] = True

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
            
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                
                if grid[nr][nc] == "1" and not visited[nr][nc]:
                    dfs(nr, nc)

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    count += 1

        return count