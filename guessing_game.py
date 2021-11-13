# GUESSING GAME

import random  # importing random module to use randInt

# letting user know about the game
print("Let’s set up our guessing game!")
print("I’ll pick a random integer between a certain min and max (inclusive) that you specify.\n")

# user input for minimum and maximum number
min_value = int(input("Min: "))
max_value = int(input("Max: "))

# input validation for maximum and minimum number
while max_value < min_value:
    max_value = int(input("The max number must be at least the min number!  Try that again: "))

# starting the game
all_values_of_i = []
user_input = 'Y'
while user_input == 'Y':
    print()
    print("OK, let's play!")
    print(f"I’m thinking of an integer between {min_value} and {max_value}, inclusive.")

    # taking a random number and a user guess input
    num_to_guess = random.randint(min_value, max_value)
    user_guess = int(input("Enter your guess: "))

    # defining while loop

    i = 0
    n = 1
    while user_guess != num_to_guess:
        if user_guess < min_value or user_guess > max_value:
            print(f"Invalid guess!  My number is between {min_value} and {max_value}.  I won’t hold it against you...")
            user_guess = int(input("Enter your guess: "))
            continue
        if user_guess > num_to_guess:
            print("Too high!  Try again...")
            user_guess = int(input("Enter your guess: "))
        else:
            print("Too low!  Try again...")
            user_guess = int(input("Enter your guess: "))
        i += 1
        n += 1

    all_values_of_i.append(n)

    # showing the result
    if i + 1 == 1:
        print(f"Woohoo, you got it!  It only took you {i + 1} try.")
        print('You should consider a career in the psychic industry.')
    else:
        print(f"Woohoo, you got it!  It only took you {i + 1} tries.")


    minimum_guess = min(all_values_of_i)
    maximum_guess = max(all_values_of_i)
    total_length = len(all_values_of_i)
    sum_of_guess = sum(all_values_of_i)

    print("\nYour stats so far: ")
    print(f"Minimum guesses taken: {minimum_guess}")
    print(f"Maximum guesses taken: {maximum_guess}")
    print(f"Average guesses taken: {(sum_of_guess / total_length):.2f}")

    print()
    user_input = input("Play again? (Y for yes, anything else for no): ")
