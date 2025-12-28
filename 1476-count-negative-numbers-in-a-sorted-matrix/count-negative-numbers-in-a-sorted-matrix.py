class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0 
        for row in grid:
            for i in reversed(range(len(row))): 
                if row[i] < 0:
                    count += 1
                else:
                    break
        return count
