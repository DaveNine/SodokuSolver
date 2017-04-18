import numpy as np
from collections import Counter
import itertools as it
import time

# Flattens the 9x9 grid into an array
def flattenBoard(board):
    return np.reshape(board, len(board)**2)

#makes the array into a 9x9 grid
def squareBoard(board):
    return np.reshape(board, (9, 9))

# Check's if the state of either a 3x3 block or vert/horizontal part
# has no duplicates -- that is, the board state is okay so far.
def stateCheck(board):
    if board.ndim is 2:
        board = flattenBoard(board)
    nonzero = board[np.where(board > 0)]
    duplicates = [item for item, count in Counter(nonzero).items() if count > 1]
    return duplicates == []

# Determines if there are any inconsistencies in the board thus far.
def boardCheck(board):
    board = squareBoard(board)
    # Check vertical and horizontal
    for t, s in zip(board, board.T):
        if (not stateCheck(s)) or (not stateCheck(t)):
            return False
            break

    #check local blocks
    for j, k in it.product(np.arange(0, 9, 3), np.arange(0, 9, 3)):
        if not stateCheck(board[j:(j+3), k:(k+3)]):
            return False
            break

    return True

def emptySpots(board):
    square = squareBoard(board)
    zero = {}
    for j, k in it.product(np.arange(0, 9), np.arange(0, 9)):
        if square[j, k] == 0:
            zero[(j,k)] = 0
    return zero

def backtrack(board):
    if len(emptySpots(board)) == 0 and boardCheck(board):
        return True

    for j, k in it.product(range(0, 9), repeat=2):
        if board[j, k] == 0:
            for num in range(1, 10):
                board[j, k] = num

                if boardCheck(board) and backtrack(board):
                    return True

            board[j, k] = 0
            return False

def solveSodoku(board):
    square = squareBoard(board)
    backtrack(square)
    return square

easy = np.array([
    0,8,0,2,0,0,4,0,0,0,0,4,3,0,0,0,6,7,2,0,0,0,7,0,3,8,0,
    5,0,0,1,0,0,0,0,0,0,3,0,5,0,4,0,9,0,0,0,0,0,0,3,0,0,5,
    0,9,8,0,3,0,0,0,2,4,7,0,0,0,9,8,0,0,0,0,5,0,0,2,0,7,0])

moderate = np.array([
    0,2,0,0,5,1,7,0,0,0,6,0,2,0,0,0,0,0,0,4,0,7,0,0,2,0,0,
    0,9,8,0,0,0,4,0,0,0,5,0,6,0,2,0,9,0,0,0,6,0,0,0,8,5,0,
    0,0,9,0,0,6,0,1,0,0,0,0,0,0,7,0,3,0,0,0,5,1,9,0,0,2,0])

difficult = np.array([
    0,0,0,0,8,0,0,1,7,6,0,0,0,0,9,3,0,0,0,3,0,1,0,0,0,2,0,
    0,0,5,0,2,0,0,0,0,0,2,1,0,0,0,4,3,0,0,0,0,0,5,0,1,0,0,
    0,5,0,0,0,6,0,9,0,0,0,3,8,0,0,0,0,1,4,7,0,0,1,0,0,0,0])

very_difficult = np.array([
    3,0,0,1,0,0,0,0,0,0,9,7,2,0,4,1,0,0,0,0,0,0,0,5,0,9,0,
    8,0,0,0,4,0,5,6,0,0,0,0,0,0,0,0,0,0,0,4,3,0,2,0,0,0,8,
    0,6,0,7,0,0,0,0,0,0,0,9,8,0,3,4,1,0,0,0,0,0,0,9,0,0,6])

now = time.time()
solved = solveSodoku(difficult)
then = time.time()
print(solved)
print("Elapsed time: {:0.02f} seconds".format(then - now))
