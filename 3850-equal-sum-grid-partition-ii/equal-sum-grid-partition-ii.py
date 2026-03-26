class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        def check(g):
            mm = len(g)
            nn = len(g[0])

            curr = 0 
            seen = {} # seen[v] = [(first_row, first_col), (last_row, last_col)]

            for i in range(mm - 1):
                for j in range(nn):   # FIXED: must include all columns
                    v = g[i][j]
                    curr += v

                    # update first and last occurrence of value v
                    if v in seen:
                        seen[v][1] = (i, j)
                    else:
                        seen[v] = [(i, j), (i, j)]
                
                # difference between bottom and top partitions
                # diff = total - 2 * curr
                diff = total - 2 * curr

                # case 1: perfect split
                if diff == 0:
                    return True

                # case 2: try removing one element from top partition
                # we need an element with value = -diff
                if -diff in seen:
                    fr, fc = seen[-diff][0]  # first occurrence
                    lr, lc = seen[-diff][1]  # last occurrence

                    # CASE A: multi-row and multi-column grid
                    # removing any one cell won't disconnect
                    if nn > 1 and i + 1 > 1:
                        return True

                    # CASE B: only one row in top partition
                    # must remove from edge (leftmost or rightmost)
                    if nn > 1 and i + 1 == 1 and (fc == 0 or lc == nn - 1):
                        return True

                    # CASE C: single column grid
                    # must remove from top or bottom edge
                    if nn == 1 and (fr == 0 or lr == i):
                        return True
            
            # no valid partition found
            return False

        m, n = len(grid), len(grid[0])

        # total sum of grid
        total = sum(sum(row) for row in grid)

        # check horizontal cuts (top → bottom)
        # and reversed (bottom → top)
        if check(grid) or check(grid[::-1]):
            return True

        # transpose grid to convert vertical cuts into horizontal cuts
        grid = list(zip(*grid))

        # check vertical cuts (left → right)
        # and reversed (right → left)
        if check(grid) or check(grid[::-1]):
            return True 

        return False