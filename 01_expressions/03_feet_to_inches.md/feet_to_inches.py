## Problem Statement

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

## Starter Code

# ```bash
# def main():
#     print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# ```

## Solution

# ```bash

# """
# An example program with constants
# """

# INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

# def main():
#     feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
#     inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
#     print("That is", inches, "inches!")
    
    
# # This provided line is required at the end of a Python file
# # to call the main() function.
# if __name__ == '__main__':
#     main()
# ```

#03_feet_to_inches.md

print("03_feet_to_inches")  # Print the program name

# Constant: 12 inches per foot
INCHES_IN_FOOT: int = 12  

def convert_feet_to_inches():
    # Get user input and convert to integer
    feet: int = int(input("Enter feet and I will convert into inches: "))  

    # Print the conversion result
    print(f"There are {feet * INCHES_IN_FOOT} inches in {feet} feet.")

# Run the function when the script is executed
if __name__ == "__main__":
    convert_feet_to_inches()
