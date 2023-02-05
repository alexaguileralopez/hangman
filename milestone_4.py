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
        self.list_of_guesses = [ ]
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))

        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word: 
            print(f"Good guess! {guess} is in the word.")
            
            for letter in self.word:
                if self.word(letter) == guess:
                    self.word_guessed[letter] = guess
            
            self.num_letters = self.num_letters - 1
        return

    def ask_for_input(self):
        while True:
            guess= input("Guess a letter: ")


            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break 
                
        #return
        
        

game1 = Hangman()

game1.ask_for_input()

            
        










