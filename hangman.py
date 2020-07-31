import random
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 0   |
     |
     |
    ===''', '''
 +---+
 0   |
 |   |
     |
    ===''', '''
 +---+
 0   |
/|   |
     |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/    |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
     |
    ===''']

words = """ant baboon bat bear beaver camel cat clam cobra cougar 
coyote crow deer dog donkey duck eagle ferret""".split()

def getRandomWord(wordList):
   wordIndex = random.randint(0, len(wordList) - 1)
   return wordList[wordIndex]