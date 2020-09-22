# Sonar Treasure Hunt

import random, sys, math

def getNewBoard():
    # Create new 60x15 data structure
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    tensDigitLine = '   '
    for i in range(1, 6):
        tensDigitLine += (' ' * 9) + str(i)

    print(tensDigitLine)
    print(' ' + ('0123456789' * 6))
    print()