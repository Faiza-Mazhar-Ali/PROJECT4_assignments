# Problem Statement
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def main():
#     # Get the numbers we want to divide
#     dividend: int = int(input("Please enter an integer to be divided: "))
#     divisor: int = int(input("Please enter an integer to divide by: "))

#     quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
#     remainder: int = dividend % divisor  # Get the remainder of the division (modulo)
    
#     print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()



#05_remainder_division.md

print("05_remainder_division")

def remainder_division():
    # Get input from user
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Perform integer division and find remainder
    quotient: int = dividend // divisor  # Integer division
    remainder: int = dividend % divisor  # Modulo operation

    # Display the results
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    remainder_division()
