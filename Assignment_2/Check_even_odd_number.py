"""
Module 3: Control Structures in Python

Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
"""
#
num = int(input("Enter the number: "))

# Using ternery operator
print("even") if num % 2 == 0 else print("odd")

# Another way to find odd-even number using if-else block
# if num % 2 == 0:
#     print("The number you entered is EVEN")
# else:
#     print("The number you entered is ODD")