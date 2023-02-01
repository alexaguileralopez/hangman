
import random

## a list with 5 fruits

word_list = ["apple", "orange", "banana", "pear", "strawberry"]

## assigning a random word to variable "word"
word = random.choice(word_list)

while True:
    guess = input('Please guess a letter: ')
    if len(guess) == 1 and guess.isalpha() == True:
        
        break
    else: 
        print("Invalid letter. Please enter a single alphabetical character")

if guess in word:
    print("Good guess!", guess, "is in the word.")
else: 
    print("Sorry,", guess, "is not in the word. Try again")