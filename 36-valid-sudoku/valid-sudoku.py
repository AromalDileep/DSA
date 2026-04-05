class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        # check cols
        for i in range(9):
            seen = set()
            for j in range(9):
                val = board[j][i]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
        
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

