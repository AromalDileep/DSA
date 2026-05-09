class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])

        layers = min(rows, cols) // 2

        for layer in range(layers):
            items = []

            # top row
            for j in range(layer, cols - layer):
                items.append(grid[layer][j])

            # right column
            for i in range(layer + 1, rows - layer - 1):
                items.append(grid[i][cols - layer - 1])

            # bottom row
            for j in range(cols - layer - 1, layer - 1, -1):
                items.append(grid[rows - layer - 1][j])

            # left column
            for i in range(rows - layer - 2, layer, -1):
                items.append(grid[i][layer])

            # rotate
            size = len(items)
            rot = k % size
            rotated = items[rot:] + items[:rot]

            idx = 0

            # put back top row
            for j in range(layer, cols - layer):
                grid[layer][j] = rotated[idx]
                idx += 1

            # put back right column
            for i in range(layer + 1, rows - layer - 1):
                grid[i][cols - layer - 1] = rotated[idx]
                idx += 1

            # put back bottom row
            for j in range(cols - layer - 1, layer - 1, -1):
                grid[rows - layer - 1][j] = rotated[idx]
                idx += 1

            # put back left column
            for i in range(rows - layer - 2, layer, -1):
                grid[i][layer] = rotated[idx]
                idx += 1

        return grid