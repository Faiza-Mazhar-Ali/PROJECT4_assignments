# ## Problem Statement

# Simulate rolling two dice, and prints results of each roll as well as the total.

# ## Starter Code

# ```bash
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# ```

# ## Solution

# ```bash
# """
# Simulate rolling two dice, and prints results of each
# roll as well as the total.
# """
# # Import the random library which lets us simulate random things like dice!
# import random

# # Number of sides on each die to roll
# NUM_SIDES: int = 6

# def main():
#     # Setting a seed is useful for debugging (uncomment the line below to do so!)
#     # random.seed(1)
    
#     # Roll die
#     die1: int = random.randint(1, NUM_SIDES)
#     die2: int = random.randint(1, NUM_SIDES)
    
#     # Get their total
#     total: int = die1 + die2
    
#     # Print out the results
#     print("Dice have", NUM_SIDES, "sides each.")
#     print("First die:", die1)
#     print("Second die:", die2)
#     print("Total of two dice:", total)


# # This provided line is required at the end of a Python file
# # to call the main() function.
# if __name__ == '__main__':
#     main()

# ```



#06_rolldice.md

import random

print("06_dice_simulator")

def roll_dice():
    # Generate two random numbers between 1 and 6 (inclusive)
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)
    
    # Calculate the total
    total: int = dice1 + dice2
    
    # Display the results
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total of two dice: {total}")

if __name__ == "__main__":
    roll_dice()
