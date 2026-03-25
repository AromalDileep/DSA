class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        
        total = sum((sum(row) for row in grid))

        if total % 2 != 0:
            return False 
        
        curr = 0 
        for i in range(m-1):
            curr += sum(grid[i])
            if curr * 2 == total:
                return True
        
        curr = 0
        for j in range(n-1):
            for i in range(m):
                curr += grid[i][j]
            
            if curr * 2 == total:
                return True 
        return False