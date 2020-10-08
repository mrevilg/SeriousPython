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

    for row in range(15):
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitLine)

def getRandomChests(numChests):
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0,14)]
        if newChest not in chests:
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    smallestDistance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - y) + (cy - y) * (cy - y))

        if distance < smallestDistance:
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return 'Treasure detected at a distance of %s from the sonar device.' % (smallestDistance)

        else:
            board[x][y] = 'X'
