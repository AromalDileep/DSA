class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_digit = set()
            for num in row:
                if num in row_digit:
                    return False
                elif num.isdigit():
                    row_digit.add(num)
        inverse = list(zip(*board))
        for row in inverse:
            row_digit = set()
            for num in row:
                if num in row_digit:
                    return False
                elif num.isdigit():
                    row_digit.add(num)

        for i in range(0, 9, 3):   # row blocks: 0, 3, 6
            for j in range(0, 9, 3):  # col blocks: 0, 3, 6
                box_digit = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i + k][j + l]
                        if num in box_digit:
                            return False
                        elif num.isdigit():
                            box_digit.add(num)
        return True

        