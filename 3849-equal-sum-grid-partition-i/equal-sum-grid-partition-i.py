class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        
        h = [sum(row) for row in grid]
        v = [sum(col) for col in zip(*grid)]

        total = sum(h)

        if total % 2 != 0:
            return False  
        
        curr = 0 
        for i in range(len(h)):
            curr += h[i]
            if curr == total - curr:
                return True 
        
        curr = 0
        for j in range(len(v)):
            curr += v[j]
            if curr == total -curr:
                return True 
        
        return False