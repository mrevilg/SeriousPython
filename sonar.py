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
            return 'Sonar did not detect anything. All chests out of range.'

def enterPlayerMove(previousMoves):
    print('Where do you want to sdrop the next sonar? (0-59 0-14 or quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('You already moved there.')
                continue
            return [int(move[0]), int(move[1])]

        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')

def showInstructions():
    print('''Instructions: You are the captain of the Simon, a treasure-hunting ship. Your cuttent
    mission is to use your devices to find sunken treasure chests at the bottom
    of the ocean. But, you only have a sonar that indicates distance, not direction!
    
    Enter the coordinates to drop a sonar device, and it will mark the map. An X indicates the chest
    is beyond the sonar range, a number indictaes how many spaces away the chest is, and a C marks
    the chest itself
    
    Press enter to continue...''')
    input()

    print('''When you drop directly on a chest, you retrieve it, and the remaing sonars update.''')

    print('Press enter to continue...')
    input()

print('S O N A R !') 
print() 
print('Would you like to view the instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    # Game loop
     

