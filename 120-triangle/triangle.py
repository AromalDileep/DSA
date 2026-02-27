class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        mem = triangle[row-1].copy()
      
        for r in range(row-2, -1, -1):
            for c in range(r+1):
                mem[c] = min(mem[c], mem[c+1]) + triangle[r][c]
        
        return mem[0]