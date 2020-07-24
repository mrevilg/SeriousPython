import random, time

def displayIntro():
    print(''' You are in a land full of dragons. I font of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon 
is greeedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave !='2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chooseCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you, he opens his jaws and...')
    print()
    time.sleep(2)