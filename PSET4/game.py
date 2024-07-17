# import random library
import random

# prompt the user for a level
# ensure that the user provides positive integer
while True:
    try:
        lvl = int(input("Level: "))
        if lvl <= 0:
            continue
        else:
            break
    except ValueError:
        continue

# random.randint(a, b) is used to give out random number a <= N <= b
randomNum = random.randint(1, lvl)

# once all the specifications are correct, let the player makes the guess
# if the guess is small, print out Too small!
# if it is large, print out Too large!
# if it is correct, print out Just right! and exit the program
# if the user makes the guess which is not the integer, let say, a string, reprompt again.
while True:
    try:
        guess = int(input("Guess: "))
        if guess == randomNum:
            print("Just right!")
            break
        elif guess < randomNum:
            print("Too small!")
        else:
            print("Too large!")
    except ValueError:
        continue