import random

## a list with 5 fruits

word_list = ["apple", "orange", "banana", "pear", "strawberry"]

print(word_list)

## assigning a random word to variable "word"
word = random.choice(word_list)

print(word)

## asking user for input

guess = input('Enter a character: ')

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess")
else: 
    print("Oops! That is not a valid input")

