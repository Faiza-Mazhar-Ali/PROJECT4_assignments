# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def read_phone_numbers():
#     """
#     Ask the user for names/numbers to story in a phonebook (dictionary).
#     Returns the phonebook.
#     """
#     phonebook = {}                   # Create empty phonebook

#     while True:
#         name = input("Name: ")
#         if name == "":
#             break
#         number = input("Number: ")
#         phonebook[name] = number

#     return phonebook


# def print_phonebook(phonebook):
#     """
#     Prints out all the names/numbers in the phonebook.
#     """
#     for name in phonebook:
#         print(str(name) + " -> " + str(phonebook[name]))


# def lookup_numbers(phonebook):
#     """
#     Allow the user to lookup phone numbers in the phonebook
#     by looking up the number associated with a name.
#     """
#     while True:
#         name = input("Enter name to lookup: ")
#         if name == "":
#             break
#         if name not in phonebook:
#             print(name + " is not in the phonebook")
#         else:
#             print(phonebook[name])


# def main():
#     phonebook = read_phone_numbers()
#     print_phonebook(phonebook)
#     lookup_numbers(phonebook)


# # Python boilerplate.
# if __name__ == '__main__':
#     main()




#01_phonebook.md
def add_contacts():
    """
    Collects names and phone numbers from the user and stores them in a dictionary.
    Returns the phonebook.
    """
    contacts = {}  # Empty dictionary to store phonebook

    while True:
        name = input("Enter name (or press Enter to stop): ").strip()
        if not name:
            break  # Stop input when user presses Enter

        number = input(f"Enter phone number for {name}: ").strip()
        contacts[name] = number  # Store name-number pair

    return contacts


def display_contacts(phonebook):
    """
    Displays all contacts stored in the phonebook.
    """
    print("\n📞 Phonebook Contacts:")
    if not phonebook:
        print("No contacts found.")
    else:
        for name, number in phonebook.items():
            print(f"{name} → {number}")


def search_contact(phonebook):
    """
    Allows user to search for a contact's number by name.
    """
    while True:
        name = input("\n🔍 Enter name to look up (or press Enter to exit): ").strip()
        if not name:
            break  # Stop searching when user presses Enter

        if name in phonebook:
            print(f"{name}'s number: {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")


def main():
    """
    Runs the phonebook program.
    """
    phonebook = add_contacts()
    display_contacts(phonebook)
    search_contact(phonebook)


if __name__ == "__main__":
    main()
