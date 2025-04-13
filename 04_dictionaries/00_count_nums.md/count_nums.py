# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def get_user_numbers():
#     """
#     Create an empty list.
#     Ask the user to input numbers and store them in a list. 
#     Once they enter a blank line, break out of the loop and return the list.
#     """
#     user_numbers = []
#     while True:
#         user_input = input("Enter a number: ")
        
#         # If the user enters a blank line, break out of the loop and stop asking for input
#         if user_input == "":
#             break
        
#         # convert the user input to an integer and add it to the list
#         num = int(user_input)
#         user_numbers.append(num)
    
#     return user_numbers

# def count_nums(num_lst):
#     """
#     Create an empty dictionary.
#     Loop over the list of numbers. 
#     If the number is not in the dictionary, add it as a key with a value of 1.
#     If the number is in the dictionary, increment its value by 1.
#     """
#     num_dict = {}
#     for num in num_lst:
#         if num not in num_dict:
#             num_dict[num] = 1
#         else:
#             num_dict[num] += 1
    
#     return num_dict


# def print_counts(num_dict):
#     """
#     Loop over the dictionary and print out each key and its value.
#     """
#     for num in num_dict:
#         print(str(num) + " appears " + str(num_dict[num]) + " times.")


# def main():
#     """
#     Ask the user to input numbers and store them in a list. Once they enter a blank line,
#     print out the number of times each number appeared in the list.
#     """
#     user_numbers = get_user_numbers()
#     num_dict = count_nums(user_numbers)
#     print_counts(num_dict)


# # Python boilerplate.
# if __name__ == '__main__':
#     main()






# 00_count_nums.md

def get_user_numbers():
    """
    Ask the user to enter numbers and store them in a list.
    Stop asking for input when the user enters a blank line.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":  # Stop when the user presses Enter
            break
        
        num = int(user_input)  # Convert to integer
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
    """
    Count how many times each number appears in the list.
    Return a dictionary with number-frequency pairs.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1  # Update count using .get()
    
    return num_dict

def print_counts(num_dict):
    """
    Print out each number and how many times it appears.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")  # Using f-string for cleaner output

def main():
    """
    Get user input, count occurrences, and print results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

# Required Python boilerplate
if __name__ == '__main__':
    main()
