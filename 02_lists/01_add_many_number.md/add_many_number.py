# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def add_many_numbers(numbers)-> int:
#     """
#     Takes in a list of numbers and returns the sum of those numbers.
#     """

#     total_so_far: int = 0
#     for number in numbers:
#         total_so_far += number

#     return total_so_far

# # There is no need to edit code beyond this point

# def main():
#     numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
#     sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
#     print(sum_of_numbers)  # Print out the sum above
    

# if __name__ == '__main__':
#     main()

#01_add_many_number.md

print("🔢 Welcome to the Number Adder! 🔢\n")

def sum_of_list(numbers: list[int]) -> int:
    """Returns the sum of a list of numbers using the built-in sum() function."""
    return sum(numbers)

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Define a sample list
    total: int = sum_of_list(numbers)  # Calculate the sum
    print(f"📊 The sum of {numbers} is ➝ {total} 🎯")  # Enhanced output

if __name__ == "__main__":
    main()
