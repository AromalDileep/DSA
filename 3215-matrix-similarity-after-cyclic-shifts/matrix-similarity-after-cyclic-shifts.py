class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m, n = len(mat), len(mat[0])
        res = [[0]*n for _ in range(m)]

        
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    res[i][(j-k) %n] = mat[i][j]
                else:
                    res[i][(j+k) %n] = mat[i][j]

        return mat == res


