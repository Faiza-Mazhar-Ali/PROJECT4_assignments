## Problem Statement

#Simulate rolling two dice, three times.  Prints the results of each die roll.  This program is used to show how variable scope works.

## Starter Code

#```bash
#def main():
 #   print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
#if __name__ == '__main__':
#    main()
#```

## Solution

#```bash
#"""
#Program: dicesimulator
#----------------------
#Simulate rolling two dice, three times.  Prints
#the results of each die roll.  This program is used
#to show how variable scope works.
#"""

# Import the random library which lets us simulate random things like dice!
#import random

# Number of sides on each die to roll
#NUM_SIDES = 6

#def roll_dice():
#    """
#   Simulates rolling two dice and prints their total
#    """
#    die1: int = random.randint(1, NUM_SIDES)
#    die2: int = random.randint(1, NUM_SIDES)
#    total: int = die1 + die2
#    print("Total of two dice:", total)

#def main():
#    die1: int = 10
#    print("die1 in main() starts as: " + str(die1))
#    roll_dice()
#    roll_dice()
#    roll_dice()
#    print("die1 in main() is: " + str(die1))

# This provided line is required at the end of a Python file
# to call the main() function.
#if __name__ == '__main__':
#    main()
#```



##01_dicesimulator.md

# Import the random module for dice simulation
import random

# Number of sides on a die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Rolled: {die1} and {die2} - Total: {total}")

def main():
    die1 = 10  # Local variable inside main()
    print(f"die1 in main() starts as: {die1}")

    # Roll the dice three times
    roll_dice()
    roll_dice()
    roll_dice()

    # The original die1 in main() remains unchanged
    print(f"die1 in main() is: {die1}")

# Run the program
if __name__ == '__main__':
    main()
