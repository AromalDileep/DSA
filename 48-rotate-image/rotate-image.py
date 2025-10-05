class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Step 1: Transpose the matrix using zip
        matrix[:] = [list(row) for row in zip(*matrix)]  # In-place update using slicing

        # Step 2: Reverse each row in place
        for row in matrix:
            row.reverse()
            