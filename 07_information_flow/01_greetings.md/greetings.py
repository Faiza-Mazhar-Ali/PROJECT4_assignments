# Problem Statement
# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

# Here's a sample run of the program (user input in bold italics):

# What's your name? Sophia

# Greetings Sophia!

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def main():
#     name : str = input("What's your name? ")
#     print(greet(name))

# # There is no need to edit code beyond this point

# def greet(name):
#     return "Greetings " + name + "!"
	
# if __name__ == '__main__':
#     main()





#01_greetings.md
def greet(person_name: str) -> None:
    """
    Prints a personalized greeting for the given name.
    """
    print(f"Hello there, {person_name}! Welcome aboard.")


def main():
    # Prompt the user for their name
    name = input("What's your name? ").strip()
    # Call the greeting helper
    greet(name)

if __name__ == '__main__':
    main()
