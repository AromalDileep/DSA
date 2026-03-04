class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        row_counts = [0] * m
        col_counts = [0] * n
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        
        res = 0
        for r in range(m):
            if row_counts[r] == 1:
                for c in range(n):
                    if mat[r][c] == 1 and col_counts[c] == 1:
                        res += 1
                        
        return res