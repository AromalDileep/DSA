class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m, n = len(mat), len(mat[0])
        k = k % n

        for i in range(m):
            if i % 2 == 0:
                if mat[i] != mat[i][k:] + mat[i][:k]:
                    return False
                
            else:
                if mat[i] != mat[i][-k:] + mat[i][:-k]:
                    return False
        return True
