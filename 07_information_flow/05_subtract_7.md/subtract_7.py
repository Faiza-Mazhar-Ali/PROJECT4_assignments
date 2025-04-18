# Problem Statement
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# def main():
# 	num: int = 7
# 	num = subtract_seven(num)
# 	print("this should be zero: ", num)

# def subtract_seven(num):
# 	num = num - 7
# 	return num


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()





#05_subtract_7.md

def reduce_by_seven(value):
    """
    Decreases the given number by 7 and returns the result.
    """
    return value - 7

def main():
    original_number = 14
    result = reduce_by_seven(original_number)
    print("After subtracting 7, the result is:", result)

if __name__ == '__main__':
    main()
