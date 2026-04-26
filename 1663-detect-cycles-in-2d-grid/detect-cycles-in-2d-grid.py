class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, pr, pc, char):
            visited[r][c] = True

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                
                if grid[nr][nc] != char:
                    continue
                
                if not visited[nr][nc]:
                    if dfs(nr, nc, r, c, char):
                        return True
                
                elif nr != pr or nc != pc:
                    return True
            
            return False
        
        for  r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    if dfs(r,c,-1,-1,grid[r][c]):
                        return True
        
        return False