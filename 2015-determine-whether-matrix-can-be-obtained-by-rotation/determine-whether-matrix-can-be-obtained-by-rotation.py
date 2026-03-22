class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        

        def rotate(mat):
            n = len(mat)
# swap top and bottom then swap diagonally for rotatin 90 degre

            # swapping top and bottom
            # for i in range(n // 2): 
            #     for j in range(n):
            #         mat[i][j], mat[n-1-i][j] = mat[n-1-i][j], mat[i][j]
            # or
            mat.reverse()

            # swapping diagonals (works for square matrix)

            for i in range(n):
                for j in range(i + 1):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            return mat == target
        
        for i in range(4):
            if rotate(mat):
                return True
        return False


