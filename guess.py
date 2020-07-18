# This is a number guess game

import random

guessesTaken = 0

print('Hi there! what is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.')
    guess =  input()
    guess = int(guess)