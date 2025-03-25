#Problem Statement
#Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

#The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

#The equation you should use for converting from Fahrenheit to Celsius is the following:

#degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

#(Note. The .0 after the 5 and 9 matters in the line above!!!)

#Here's a sample run of the program (user input is in bold italics):

#Enter temperature in Fahrenheit: 76

#Temperature: 76.0F = 24.444444444444443C

#Starter Code
#def main():
 #   print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
#if __name__ == '__main__':
 #   main()
#Solution


#03_fahrenheit_to_celsius.md

def convert_temperature():
    # Ask for temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Print the result
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

# This is required when running as a Python script in VS Code
if __name__ == '__main__':
    convert_temperature()
