class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        res = set()
        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):

                res.add(grid[row][col])  

                size = 1
                while row - 2*size >= 0 and col - size >= 0 and col + size < n:

                    total = 0

                    for i in range(size):
                        # bottom -> left
                        total += grid[row - i][col - i]
                        # left -> top
                        total += grid[row - size - i][col - size + i]
                        # top -> right
                        total += grid[row - 2*size + i][col + i]
                        # right -> bottom
                        total += grid[row - size + i][col + size - i]

                    res.add(total)

                    size += 1

        return sorted(res, reverse=True)[:3]