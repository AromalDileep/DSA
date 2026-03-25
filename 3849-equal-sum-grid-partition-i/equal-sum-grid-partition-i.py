class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        
        h = [sum(row) for row in grid]
        v = [sum(col) for col in zip(*grid)]

        total = sum(h)

        if total % 2 != 0:
            return False  
        
        curr = 0 
        for i in range(len(h)-1): # m-1 or len(h)-1 because no need to cut after last row
            curr += h[i]
            if curr * 2 == total:
                return True 
        
        curr = 0
        for j in range(len(v)-1):
            curr += v[j]
            if curr *2 == total:
                return True 
        
        return False