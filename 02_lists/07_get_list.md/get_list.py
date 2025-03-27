# Problem Statement
# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def main():
#     lst = []  # Make an empty list to store things in

#     val = input("Enter a value: ")  # Get an initial value
#     while val:  # While the user input isn't an empty value
#         lst.append(val) # Add val to list
#         val = input("Enter a value: ")  # Get the next value to add

#     print("Here's the list:", lst)


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()



#07_get_list.md
def collect_values():
    """
    Collects values from the user until they press Enter, then returns the list.
    """
    values = []
    while True:
        user_input = input("Enter a value (or press Enter to finish): ")
        if user_input == "":  # Stop when the user presses Enter without input
            break
        values.append(user_input)  # Add input to the list
    return values

def main():
    user_list = collect_values()
    print("Here is your list:", user_list)

if __name__ == '__main__':
    main()

