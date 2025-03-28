# ## Problem Statement

# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28
# 30
# 32
# 34
# 36
# 38

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
# def main():
#     # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
#     for i in range(20):
#         print(i * 2)  # Use the 'i' value inside the for-loop
   
# # Call the main function when "run", no need to edit anything below!
# if __name__ == "__main__":
#     main()


#01_print_events.md

def print_even_numbers(count):
    """
    Prints the first `count` even numbers.
    """
    num = 0
    for _ in range(count):
        print(num)
        num += 2  # Increment by 2 to get the next even number

def main():
    total_even_numbers = 20  # Define the total number of even numbers to print
    print_even_numbers(total_even_numbers)

if __name__ == '__main__':
    main()
