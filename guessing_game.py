"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
solution = random.randint(1, 10)
# random module info from https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python

def start_game():
    

    print("------------------------------------" +"\n" + "Welcome to the number guessing game!" +"\n" "------------------------------------")

    while True:
        try:
            guess = int(input("Pick a number between 1 and 10:  "))
            print ("Your guess is {}".format(guess))
            print ("The answer is {}".format(solution))
        except ValueError as err:
            # print("({})".format(err))
            print ("You must enter a number, please try again")
            continue #do I need this here?
        if guess < solution:
            print("It's higher !") 
            continue
        elif guess > solution:
            print("It's lower !") 
            continue

        elif guess == solution:
            print ("Correct!")
            break





        





    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.






if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
