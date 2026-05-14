from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    # check for duplicates by row
    for row in board:
        string = "".join(char for char in row if char != ".")
        if len(string) != len(set(string)):
            return False
    # check for duplicates by col
    for col in range(9):
        string = ""
        for row in range(9):
            string += board[row][col] if board[row][col] != "." else ""
        if len(string) != len(set(string)):
            return False
    # check for duplicates by 3x3 grid
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            string = ""
            for i in range(r, r+3):
                for j in range(c, c+3):
                    string += board[i][j] if board[i][j] != "." else ""
            if len(string) != len(set(string)):
                return False
    return True

# Test Case #1
# Output: False
board =[[".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(board))


# Test Case #2
# Output: True
board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))


