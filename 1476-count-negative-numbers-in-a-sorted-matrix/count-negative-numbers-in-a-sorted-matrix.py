class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid) - 1, 0
        cols = len(grid[0])
        count = 0

        while m >= 0 and n < cols:
            if grid[m][n] < 0:
                count += (cols - n)   
                m -= 1
            else:
                n += 1
        
        return count
