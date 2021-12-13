import os
import sys
import copy
from time import sleep

NUM_GENS = 10



# A function to print out a 2D array
def printBoard(arr, gen):
    # print the generation number
    print(f"Generation {gen}")

    print(" ", end = " ")
    # print the header row
    for i in range(1, size-1):
        #print("{}".format(i))
        print(f"{i%10}", end = " ")
    print()

    # print each row of information after the row number
    for row in range(1, size-1):
        print(f"{row%10}", end = " ")
        for col in range(size):
            print(board[row][col], end = " ")
        print()

# this function applies the rules of the game of life to create a new
# board with the appropriate cells
def computeNextGen(arr):
    newboard = copyBoard(arr)

    for row in range(1, size-1):
        for col in range(1, size-1):
            neighbours = countNeighbours(arr, row, col)
            
            if (arr[row][col] == "*"):
                if (neighbours < 2 or neighbours > 3):
                    newboard[row][col] = " "
            else:
                if (neighbours == 3):
                    newboard[row][col] = "*"

    return newboard

# a function to create a copy of a two dimensional array
def copyBoard(arr):
    return copy.deepcopy(arr)

# a function to count the number of neighbours around a specific cell in
# the board.
def countNeighbours(arr, row, col):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (not(i == 0 and j == 0)):
                if (arr[row+i][col+j] == "*"):
                    neighbours += 1


    return neighbours

# main program
board = []

# read the file and store it in an array
for line in sys.stdin:
    size = len(line) - 1
    board.append([])
    for i in range(size):
        board[len(board)-1].append(line[i])

try:
    for i in range(NUM_GENS):
        os.system("clear")
        #os.system("cls")
        # then print it out
        printBoard(board, i)
        sleep(1)
        # update to get the next generation
        board = computeNextGen(board)
except KeyboardInterrupt:
    print("Done")
