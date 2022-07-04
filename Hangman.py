import random

amountHint = 0
HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        |
===========''', '''


    +---+
    |   |
    O   |
    |   |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
   L    |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
   L  L |
        |
===========''']

words = {
    'Animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pidgeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
    'Fruits': 'apple banana blackberry blueberry cherry cranberry durian grapefruit grape guava honeydew jackfruit kiwi lemon lime mandarin mango olives orange papaya peach pear pineapple plum pomegranate prune rasberry strawberry tangerine watermelon'.split(),
    'Colors': 'aquamarine black blue brown cyan green gray indigo lime magenta maroon navy olive orange pink purple red silver tan teal turquoise violet white yellow'.split()}


def getRandomWord(wordDict):
    wordKey = getSet(wordDict)
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):

        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def getSet(wordDict):
    key = ""
    while True:
        print('Choose a set of words: ', end='')
        keys = list(wordDict.keys())
        for i in range(len(keys)):
            print(keys[i] + "(" + str(i + 1) + ")", end=" ")
        print()
        set = input()
        if set.isdigit():
            set = int(set)
            if (set > len(keys) or set <= 0):
                print('Please enter a number between 1 and ' + str(len(keys)))
            else:
                key = keys[set - 1]
                break
        else:
            print('Please enter a NUMBER.')

    return key


# Given a secret word - Apple
# You guessed e         ____e

# create variable potential hint
# Iterate (for loop) through secret word
# check if the character is already guess
# if not add it to list of potential hint
# After the for loop return a random character from the potential hint

# Print the hint
def getHint(correctLetters, secretWord):
    potential_hint = ''
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            potential_hint = potential_hint + secretWord[i]
    return potential_hint[random.randint(0, len(potential_hint) - 1)]
    # return random.choice(potential_hint)


#    for i in range(len(secretWord)):
#        if secretWord[i] not in correctLetters:
#            hint = secretWord[i]
#            return hint


#    HINT do something similar to below probably opposite to get list of characters in secret word that is not in correct letters
#    for i in range(len(secretWord)):
#        if secretWord[i] in correctLetters:
#            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

def getGuess(missedLetters, correctLetters, secretWord):
    global amountHint
    alreadyGuessed = missedLetters + correctLetters
    while True:
        print('Guess a letter. Type ? for hint. You only have {} hints.'.format(3 - amountHint))
        guess = input()
        guess = guess.lower()
        if len(guess)!=1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif (guess=='?') and amountHint < 3:
            print('Your hint is: ' + str(getHint(correctLetters, secretWord)))
            amountHint = amountHint + 1
            print('You have {} hints remaining.'.format(3 - amountHint))
        elif (guess=='?') and amountHint >= 3:
            print('You have no hints left.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''

secretWord, secretKey = getRandomWord(words)
gameIsDone = False

while True:

    print('The secret word is in the set: ' + secretKey)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters, correctLetters, secretWord)
    print("Guessed a letter: ", guess)
    if guess in secretWord:
        print("Guessted letter is in the secret word")
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is ' + secretWord + '! You have won!')
            gameIsDone = True
    else:
        print("Guessted letter is NOT in the secret word")
        missedLetters = missedLetters + guess

        if len(missedLetters)==len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretKey = getRandomWord(words)
        else:
            break