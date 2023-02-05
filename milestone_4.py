import random

class Hangman():
    # class constructor    

    word_list = ["apple", "orange", "banana", "pear", "strawberry"]
    
    def __init__(self, word_list = word_list, num_lives=5): #the number of lives is set to a default value of 5
       
       # There is some problem, as various of the defined attributes are not recognised in the methods
       # that are defined afterwards

        #attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))

        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word: #at the moment, it does not recognise word from the init method
            print("Good guess!", guess, "is in the word.")
        return

    def ask_for_input(self):
        while True:
            user_input= input("Enter a character: ")
            if len(user_input) != 1 or user_input.isalpha() == False:
                print("Please, enter a single alphabetical character")
            elif user_input in self.list_of_guesses: # does not recognise list_of_guesses frmo the init method
                print("You already tried that letter")
            else: 
                self.check_guess(user_input) # does not recognise check_guess from the method defined just before
                break
        return
        
        

game1 = Hangman()

game1.ask_for_input()
            
        










