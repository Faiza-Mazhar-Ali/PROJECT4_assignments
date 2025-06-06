# Problem Statement
# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def print_ones_digit(num): print("The ones digit is", num % 10)

# def main(): num = int(input("Enter a number: ")) print_ones_digit(num)

# There is no need to edit code beyond this point
# if name == 'main': main()




#10_print_ones_digit.md
def show_ones_digit(value: int) -> None:
    """
    Prints the ones (units) digit of the given integer.
    """
    digit = abs(value) % 10
    print(f"The one's digit of {value} is {digit}.")

def main():
    user_input = input("Please enter an integer: ").strip()
    try:
        number = int(user_input)
        show_ones_digit(number)
    except ValueError:
        print("Oops! That wasn’t an integer. Please try again.")

if __name__ == '__main__':
    main()
