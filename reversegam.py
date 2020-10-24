
import random, sys

WIDTH = 8
HEIGHT = 8

def drawBoard(board):
    print(' 123456789')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('%s|' % (y+1))
    print(' +--------+')    
    print(' 123456789')

def getNewBoard():