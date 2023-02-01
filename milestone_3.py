
while True:
    guess = input('Please guess a letter: ')
    if len(guess) == 1 and guess.isalpha() == True:
        print("Valid")
        break
    else: 
        print("Invalid letter. Please enter a single alphabetical character")

