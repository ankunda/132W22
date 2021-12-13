import sys

board = []

for line in sys.stdin:
    board.append([])
    for char in line:
        board[len(board)-1].append(char)

print(board)
