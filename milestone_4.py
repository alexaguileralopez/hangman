import random

class Hangman():
    # class constructor
    def __init__(self, word_list, num_lives=5): #the number of lives is set to a default value of 5

        #attributes
        self.word_list = ["apple", "orange", "banana", "pear", "strawberry"]
        self.list_of_guesses = [None]
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)

        self.num_letters = len(self.word)

        self.num_lives = num_lives





