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
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
parrot pigeon python lion lizard llama mole monkey moose mouse mule newt otter
owl panda rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake
spider stork swan tiger toad trout turkey turtle weasel whale wolf zebra""".split()

def getRandomWord(wordList):
   wordIndex = random.randint(0, len(wordList) - 1)
   return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
   print(HANGMAN_PICS[len(missedLetters)])
   print

   print('Missed letters:', end=' ')
   for letter in missedLetters:
      print(letter, end=' ')
   print()

   blanks = '_' * len(secretWord)

   for i in range(len(secretWord)):
      if secretWord[i] in correctLetters:
         blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

   for letter in blanks:
      print(letter, end=' ')
   print()

def getGuess(alreadyGuessed):
   while True:
      print('Guess a letter.')
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
         print('Please enter a sinlge letter.')
      elif guess in alreadyGuessed:
         print('You have already guessed that letter. Choose again.')
      elif guess not in 'abcdefghijklmonpqrstuvwxyz':
         print('Please enter a LETTER.')
      else:
         return guess

def playAgain():
   print('Do you want to play? (yes or no)')
   return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
   displayBoard(missedLetters, correctLetters, secretWord)

   guess = getGuess(missedLetters + correctLetters)

   if guess in secretWord:
      correctLetters = correctLetters + guess

      foundAllLetters = True
      for i in range(len(secretWord)):
         if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break
      if foundAllLetters:
         print('Yes! The secret word is "' + secretWord + '"! You won!')
         gameIsDone = True
   
   else:
      missedLetters = missedLetters + guess