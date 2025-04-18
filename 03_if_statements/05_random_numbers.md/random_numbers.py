# ## Problem Statement

# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45
# 79
# 61
# 47
# 52
# 10
# 16
# 83
# 19
# 12

# Each time you run your program you should get different numbers

# 81
# 76
# 70
# 1
# 27
# 63
# 96
# 100
# 32
# 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)

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

# import random

# N_NUMBERS : int = 10
# MIN_VALUE : int = 1
# MAX_VALUE : int = 100

# def main():
#     """
#     You should write your code here. Make sure to delete 
#     the 'pass' line before starting to write your own code.
#     """
#     pass

# if __name__ == '__main__':
#     main()
# ```


#05_random_numbers.md

import random

N_NUMBERS = 10  # Number of random numbers to generate
MIN_VALUE = 1   # Minimum value (inclusive)
MAX_VALUE = 100 # Maximum value (inclusive)

def main():
    for _ in range(N_NUMBERS):  # Loop 10 times
        print(random.randint(MIN_VALUE, MAX_VALUE))  # Generate and print a random number

if __name__ == '__main__':
    main()
