# Hangman
Text-Based Hangman game

Example gameplay below:

```
H A N G M A N
Choose a set of words: Animals(1) Fruits(2) Colors(3)
1
The secret word is in the set: Animals


    +---+
    |   |
        |
        |
        |
        |
        |
===========

Missed letters:
_ _ _ _ _ _ _
Guess a letter. Type ? for hint. You only have 3 hints.
a
Guessed a letter:  a
Guessted letter is NOT in the secret word
The secret word is in the set: Animals


    +---+
    |   |
    O   |
        |
        |
        |
        |
===========

Missed letters: a
_ _ _ _ _ _ _
Guess a letter. Type ? for hint. You only have 3 hints.
e
Guessed a letter:  e
Guessted letter is in the secret word
The secret word is in the set: Animals


    +---+
    |   |
    O   |
        |
        |
        |
        |
===========

Missed letters: a
_ _ _ _ e _ _
Guess a letter. Type ? for hint. You only have 3 hints.
o
Guessed a letter:  o
Guessted letter is in the secret word
The secret word is in the set: Animals


    +---+
    |   |
    O   |
        |
        |
        |
        |
===========

Missed letters: a
_ _ _ _ e o _
Guess a letter. Type ? for hint. You only have 3 hints.
c
Guessed a letter:  c
Guessted letter is NOT in the secret word
The secret word is in the set: Animals



    +---+
    |   |
    O   |
    |   |
        |
        |
        |
===========

Missed letters: a c
_ _ _ _ e o _
Guess a letter. Type ? for hint. You only have 3 hints.
h
Guessed a letter:  h
Guessted letter is NOT in the secret word
The secret word is in the set: Animals


    +---+
    |   |
    O   |
   /|   |
        |
        |
        |
===========

Missed letters: a c h
_ _ _ _ e o _
Guess a letter. Type ? for hint. You only have 3 hints.
r
Guessed a letter:  r
Guessted letter is NOT in the secret word
The secret word is in the set: Animals


    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
===========

Missed letters: a c h r
_ _ _ _ e o _
Guess a letter. Type ? for hint. You only have 3 hints.
?
Your hint is: n
You have 2 hints remaining.
Guess a letter. Type ? for hint. You only have 2 hints.
n
Guessed a letter:  n
Guessted letter is in the secret word
The secret word is in the set: Animals


    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
===========

Missed letters: a c h r
_ _ _ _ e o n
Guess a letter. Type ? for hint. You only have 2 hints.
?
Your hint is: d
You have 1 hints remaining.
Guess a letter. Type ? for hint. You only have 1 hints.
d
Guessed a letter:  d
Guessted letter is in the secret word
The secret word is in the set: Animals


    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
===========

Missed letters: a c h r
_ _ d _ e o n
Guess a letter. Type ? for hint. You only have 1 hints.
p
Guessed a letter:  p
Guessted letter is in the secret word
The secret word is in the set: Animals


    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
===========

Missed letters: a c h r
p _ d _ e o n
Guess a letter. Type ? for hint. You only have 1 hints.
i
Guessed a letter:  i
Guessted letter is in the secret word
The secret word is in the set: Animals


    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
===========

Missed letters: a c h r
p i d _ e o n
Guess a letter. Type ? for hint. You only have 1 hints.
g
Guessed a letter:  g
Guessted letter is in the secret word
Yes! The secret word is pidgeon! You have won!
Do you want to play again? (yes or no)
no
```
