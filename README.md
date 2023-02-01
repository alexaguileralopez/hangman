"# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 2
<ol>
  <li> Task 1: In this task, a list of 5 fruits was defined as a list of strings (word_list). Then, it was printed out using the print command. 
  <li> Task 2: The "random" library was imported, and its function "random.choice()" was used to get a random choice within the list of fruits previously created. 
  <li> Task 3: The user was asked for an input, which was assigned to a variable "guess". 
  <li> Task 4: The input was checked to be a correct input, checking if the length was equal to 1, and checking if it had an alphabetical value.
  <li> Task 5: Typing this document. 
</ol>

# Milestone 3

<ol>
  <li> Task 1: In this task, the objective is to iteratively check if the input is a valid guess. For that, a while loop with condition set to true is created. In the body of that loop, a variable called guess is assigned to the input of the user. And an if statement is created to check 1: if the input length is equal to 1 (as it should be a single character), 2: if that input is an alphabetical value with the method isalpha().
  <li> Task 2: In this task, the objective is to check wether the guess is in the word randonmly chosen by the computer. To do so, an if statement is created to check if the guess is contained within that randomly selected word. If the statement is correct, "Good guess, {guess} is in the word" is printed out. If that is not correct, "Sorry, {guess} is not in the word is printed out"
  <li> Task 3: The objective of this task is to create functions to run those checks. Two functions are created: 
    <ol>
      <ul> check_guess: takes the guessed letter as an argument and checks if the letter is in the word. This function takes in the guess as a parameter for the function. It converts this guess into lowercase and uses the code in task 2 to check if the letter is in the word.
      <ul>ask_for_input: this function uses the code in task 1, using the guess as an argument to the method.
  
  
