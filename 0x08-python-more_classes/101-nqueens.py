#!/usr/bin/python3
import sys


def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(board, queens_left):
        if queens_left == 0:
            print_board(board)
            return True
        for i in range(n):
            if is_valid(board, i):
                board.append(i)
                if solve(board, queens_left - 1):
                    return True
                board.pop()
        return False

    def is_valid(board, col):
        row = len(board)
        for i, j in enumerate(board):
            if j == col or i - j == row - col or i + j == row + col:
                return False
        return True

    def print_board(board):
        for i in range(n):
            row = ""
            for j in range(n):
                if j == board[i]:
                    row += "Q "
                else:
                    row += ". "
            print(row)
        print("")

    solve([], n)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

nqueens(n)
