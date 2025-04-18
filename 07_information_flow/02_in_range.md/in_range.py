# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def in_range(n, low, high):
#   """
#   Returns True if n is between low and high, inclusive. 
#   high is guaranteed to be greater than low.
#   """
#     if n >= low and n <= high:
# 	return True

#     # we could have also included an else statement, but since we are returning, it's fine without!
#     return False



 #02_in_range.md
def in_range(n: int, low: int, high: int) -> bool:
    """
    Determine if `n` falls within the range [low, high], inclusive.
    :param n: number to test
    :param low: lower bound
    :param high: upper bound (guaranteed >= low)
    :return: True if n is between low and high (inclusive), False otherwise
    """
    return low <= n <= high


def main():
    # Ask the user for the number to test and the bounds
    try:
        number = int(input("Enter a number to test: "))
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
    except ValueError:
        print("Invalid input! Please enter integer values.")
        return

    # Use the helper function and display the appropriate message
    if in_range(number, lower_bound, upper_bound):
        print(f"{number} is within the range {lower_bound} to {upper_bound}, inclusive.")
    else:
        print(f"{number} is outside the range {lower_bound} to {upper_bound}.")

# Boilerplate to call main()
if __name__ == '__main__':
    main()
