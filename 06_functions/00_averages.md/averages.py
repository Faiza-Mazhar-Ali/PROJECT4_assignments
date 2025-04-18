# Problem Statement
# Write a function that takes two numbers and finds the average between the two.

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def average(a: float, b: float):
#     """
#     Returns the number which is half way between a and b
#     """
#     sum = a + b
#     return sum / 2

# def main():
#     avg_1 = average(0, 10)
#     avg_2 = average(8, 10)
    
#     final = average(avg_1, avg_2)
#     print("avg_1", avg_1)
#     print("avg_2", avg_2)
#     print("final", final)
    

# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()





#averages.md
def average(a: float, b: float) -> float:
    """
    Calculates and returns the average of two numbers.
    """
    return (a + b) / 2

def main():
    print("🔢 Average Calculator")

    # Ask user for the first number
    num1 = float(input("Enter the first number: "))
    # Ask user for the second number
    num2 = float(input("Enter the second number: "))

    # Calculate the average using the function
    result = average(num1, num2)

    # Display the result
    print(f"The average of {num1} and {num2} is: {result}")

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()

