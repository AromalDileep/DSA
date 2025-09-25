class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from second last row, move upward
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Add the min path from the next row
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
        
        return triangle[0][0]
