class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows and cols
        for i in range(9):
            row_seen = set()
            col_seen = set()
            for j in range(9):
                row_val = board[i][j]
                col_val = board[j][i]
                if row_val != ".":
                    if row_val in row_seen:
                        return False
                    row_seen.add(row_val)
                if col_val != ".":
                    if col_val in col_seen:
                        return False
                    col_seen.add(col_val)

        
        # check boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()

                for i in range(3):
                    for j in range(3):
                        val = board[row + i][col +j]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)
        return True 

