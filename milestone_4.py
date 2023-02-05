import random

class Hangman():
    # class constructor    

    word_list = ["apple", "orange", "banana", "pear", "strawberry"]
    
    def __init__(self, word_list = word_list, num_lives=5): #the number of lives is set to a default value of 5
       

        #attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = [ ]
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))

    #the check_guess method checks if the guess is in the word or not. Then, it appends the "list of guesses"
    # attribute list with the guess that was taken
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word: 
            print(f"Good guess! {guess} is in the word.")
            
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess
                    #print(self.word_guessed)
                    
            self.num_letters = self.num_letters - 1
            #print(self.num_letters)
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        self.list_of_guesses.append(guess)
        return

    # this method asks the user for input and checks if the input given is valid or not
    # if it is valid, it leads the program into the check_guess method
    def ask_for_input(self):
        while True:
            guess= input("Guess a letter: ")


            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.check_guess(guess)
                
                break 
                
              

game1 = Hangman()

game1.ask_for_input()

            
        










