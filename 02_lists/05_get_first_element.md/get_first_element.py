# # ## Problem Statement

# # Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# # ## Starter Code

# # ```bash
# # def main():
# #     print("Delete this line and write your code here! :)")


# # # This provided line is required at the end of
# # # Python file to call the main() function.
# # if __name__ == '__main__':
# #     main()
# # ```

# # ## Solution

# # ```bash

# # def get_first_element(lst):
# #     """
# #     Prints the first element of a provided list.
# #     """

# #     print(lst[0])

# # # There is no need to edit code beyond this point

# # def get_lst():
# #     """
# #     Prompts the user to enter one element of the list at a time and returns the resulting list.
# #     """
# #     lst = []
# #     elem: str = input("Please enter an element of the list or press enter to stop. ")
# #     while elem != "":
# #         lst.append(elem)
# #         elem = input("Please enter an element of the list or press enter to stop. ")
# #     return lst

# # def main():
# #     lst = get_lst()
# #     get_first_element(lst)


# # if __name__ == '__main__':
# #     main()


# # ```

# #05_get_first_element.md

# ## Problem Statement

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

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

# def get_first_element(lst):
#     """
#     Prints the first element of a provided list.
#     """

#     print(lst[0])

# # There is no need to edit code beyond this point

# def get_lst():
#     """
#     Prompts the user to enter one element of the list at a time and returns the resulting list.
#     """
#     lst = []
#     elem: str = input("Please enter an element of the list or press enter to stop. ")
#     while elem != "":
#         lst.append(elem)
#         elem = input("Please enter an element of the list or press enter to stop. ")
#     return lst

# def main():
#     lst = get_lst()
#     get_first_element(lst)


# if __name__ == '__main__':
#     main()


# ```

#05_get_first_element.md

def show_first_item(data_list):
    """
    Displays the first item from the given list.
    """
    print("The first item is:", data_list[0])

def gather_inputs():
    """
    Collects user input to create a list, stopping when the user enters nothing.
    """
    elements = []
    while True:
        entry = input("Enter a value (press Enter to stop): ")
        if not entry:
            break
        elements.append(entry)
    return elements

def main():
    user_data = gather_inputs()
    show_first_item(user_data)

if __name__ == "__main__":
    main()
