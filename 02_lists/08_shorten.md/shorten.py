# ## Problem Statement

# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

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
# MAX_LENGTH : int = 3

# def shorten(lst):
#     while len(lst) > MAX_LENGTH:
#         last_elem = lst.pop()
#         print(last_elem)

# # There is no need to edit code beyond this point

# def get_lst():
#     """
#     Prompts the user to enter one element of the list at a time and returns the resulting list.
#     """
#     lst = []
#     elem = input("Please enter an element of the list or press enter to stop. ")
#     while elem != "":
#         lst.append(elem)
#         elem = input("Please enter an element of the list or press enter to stop. ")
#     return lst

# def main():
#     lst = get_lst()
#     shorten(lst)


# if __name__ == '__main__':
#     main()
# ```



#08_shorten.md

MAX_LENGTH = 3  # Define the maximum allowed length of the list

def shorten_list(lst):
    """
    Removes elements from the end of lst until its length is MAX_LENGTH.
    Prints each removed element.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def collect_input():
    """
    Collects user input to create a list.
    """
    user_list = []
    while True:
        item = input("Enter an element (or press Enter to stop): ")
        if not item:
            break
        user_list.append(item)
    return user_list

def main():
    user_list = collect_input()
    shorten_list(user_list)
    print("Final list:", user_list)  # Display the modified list

if __name__ == '__main__':
    main()
