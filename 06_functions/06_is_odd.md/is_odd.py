# Problem Statement
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def main():
#     for i in range(10):
#         if is_odd(i):
#             print('odd')
#         else:
#             print('even')
            
# def is_odd(value: int):
#     """
#     Checks to see if a value is odd. If it is, returns true.
#     """
    
#     remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
#     return remainder == 1


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()




#06_is_odd.md
def is_even(n):
    return n % 2 == 0

def print_even_odd():
    for number in range(10, 20):
        label = "even" if is_even(number) else "odd"
        print(f"{number} {label}", end=" ")

def main():
    print_even_odd()

# Standard Python entry point
if __name__ == '__main__':
    main()
