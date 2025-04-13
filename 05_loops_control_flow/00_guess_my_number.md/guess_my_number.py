# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# import random

# def main():
#     # Generate the secret number at random!
#     secret_number = random.randint(1, 99)
    
#     print("I am thinking of a number between 1 and 99...")
    
#     # Get user's guess
#     guess = int(input("Enter a guess: "))
#     # True if guess is not equal to secret number
#     while guess != secret_number:
#         if guess < secret_number:  # If-statement is True if guess is less than secret number
#             print("Your guess is too low")
#         else:
#             print("Your guess is too high")
            
#         print() # Print an empty line to tidy up the console for new guesses
#         guess = int(input("Enter a new guess: "))  # Get a new guess from the user
        
#     print("Congrats! The number was: " + str(secret_number))
    
# if __name__ == '__main__':
#     main()





#00_guess_my_number.md

import random

def main():
    number_to_guess = random.randint(1, 99)
    print("🔢 I'm thinking of a number between 1 and 99... Can you guess it?")
    
    while True:
        try:
            user_input = int(input("➡️ Your guess: "))
        except ValueError:
            print("❗ Please enter a valid number!")
            continue
        
        if user_input == number_to_guess:
            print(f"🎉 Correct! The number was: {number_to_guess}")
            break
        elif user_input < number_to_guess:
            print("📉 Too low! Try again.")
        else:
            print("📈 Too high! Try again.")
            
        print()  # Blank line for cleaner formatting

if __name__ == '__main__':
    main()
