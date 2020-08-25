import random

def drawBoard(board):
    # Prints out board.
    # "Board" = List of 10 strings

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le): # bo is board, le is letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le)
    (bo[4] == le and bo[5] == le and bo[6] == le)
    (bo[1] == le and bo[2] == le and bo[3] == le)
    (bo[7] == le and bo[4] == le and bo[1] == le)
    (bo[8] == le and bo[5] == le and bo[2] == le)
    (bo[9] == le and bo[6] == le and bo[3] == le)
    (bo[7] == le and bo[5] == le and bo[3] == le)
    (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        board.Copy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '