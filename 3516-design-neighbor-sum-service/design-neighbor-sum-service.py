class NeighborSum:
    # Original code 
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(self.grid)
        self.mp = {}
        self.iv = {}
        for row in range(self.n):
            for col in range(self.n):
                self.mp[grid[row][col]] = (row, col)
                self.iv[(row, col)] = grid[row][col]

    def adjacentSum(self, value: int) -> int:
        row, col = self.mp[value]
        top, bottom, left, right = (
            self.iv.get((row - 1, col), 0),
            self.iv.get((row + 1, col), 0),
            self.iv.get((row, col - 1), 0),
            self.iv.get((row, col + 1), 0),
        )
        return top + bottom + left + right

    def diagonalSum(self, value: int) -> int:
        row, col = self.mp[value]
        topl, topr, bottoml, bottomr = (
            self.iv.get((row - 1, col - 1), 0),
            self.iv.get((row - 1, col + 1), 0),
            self.iv.get((row + 1, col - 1), 0),
            self.iv.get((row + 1, col + 1), 0),
        )
        return topl + topr + bottoml + bottomr

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)