import random
# Imports random module to generate a random number.


def guessing_agent(low, high, secret):
    # Defines the guessing agent function.
    # low = Minimum number.
    # high = Maximum number.
    # secret = Hidden number to find.

    attempts = 0
    # Initializes the attempt counter to zero.

    while low <= high:
        # Repeats while the search range is valid.

        guess = (low + high) // 2
        # Calculates the middle number using floor division.

        attempts += 1
        # Increases the attempt counter by one.

        print(f"Attempt {attempts}: Agent guesses {guess}")
        # Displays attempt number and guessed value.

        if guess == secret:
            # Checks whether guessed number is correct.

            print(f"Correct! Number found in {attempts} attempts.")
            # Displays success message.

            return attempts
            # Returns the total number of attempts.

        elif guess < secret:
            # Checks whether guessed number is smaller than secret.

            print("Feedback: Higher")
            # Tells the agent to guess a higher number.

            low = guess + 1
            # Updates the lower limit.

        else:
            # Executes when guessed number is greater than secret.

            print("Feedback: Lower")
            # Tells the agent to guess a lower number.

            high = guess - 1
            # Updates the upper limit.

    return -1
    # Returns -1 if the number is not found.


# Main program
if __name__ == "__main__":
    # Checks whether this file is running directly.

    low, high = 1, 100
    # Sets the guessing range from 1 to 100.

    secret = random.randint(low, high)
    # Generates a random integer between 1 and 100.
    # Both limits are included.

    guessing_agent(low, high, secret)
    # Calls the guessing agent function.
