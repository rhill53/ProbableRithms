"""
CS4050 Algorithms
Spring 2020
8 queens problem
Robb Hill
"""
glued_queens = 4
queens = 8-glued_queens


def place_queens(board, col):
    # base case: If all queens are placed
    # then return true
    if col >= 8:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(8):

        if collisions(board, i, col):

            board[i][col] = 'Q'

            if place_queens(board, col + 1) == True:
                return True

            board[i][col] = '-'

    return False


def collisions(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, queens, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve():
    board = [["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-"]]

    if place_queens(board, 0) == False:
        print("Solution does not exist")
        return False

    print_board(board)
    return True


def print_board(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end = " ")
        print()


solve()
