import random

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can
totally do that by clicking:
File -> Download Workspace in the file menu after you
fork the snapshot of this workspace.

"""
"""Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution,
      display to the player "It's lower".
      b. If the guess is less than the solution,
      display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates
    the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
# write your code inside this function.


def start_game():
    attempts = 0
    highscores = []
    solution = random.randint(1, 10)
# random module info from
# https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
    print("\n" + "------------------------------------" + "\n" +
                 "Welcome to the number guessing game!" +
                 "\n" "------------------------------------" + "\n")
    while True:
        try:
            guess = int(input("Pick a number between 1 and 10:  "))
        except ValueError:
            print("You must enter a whole number, please try again.")
            continue

        if guess < 1 or guess > 10:
            # Answer ouside range
            print("Your guess is outside the range. Please try again.")
            continue
        elif guess < solution:
            # Answer too low
            attempts += 1
            print("It's higher!")
            continue
        elif guess > solution:
            # Answer too high
            attempts += 1
            print("It's lower!")
            continue
        elif guess == solution:
            # Correct answer given
            attempts += 1
            highscores.append(attempts)
            if attempts == 1:
                print("Got it! It took you {} try.".format(attempts))
            else:
                print("Got it! It took you {} tries.".format(attempts))
            restart = input("Would you like to play again [y]es/[n]o:  ")
            if restart.lower() == "y":
                # restart the game
                # Python List min() method from
                # https://www.tutorialspoint.com/python/list_min.htm
                print("\n" + "The HIGHSCORE is {}".format(min(highscores)))
# reset the solution and attempt counts
                solution = random.randint(1, 10)
                attempts = 0
                continue
            else:
                print("Closing game, see you next time!" + "\n")
                break


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
