'''
Task 2: Using the Math Module for Calculations

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

'''
import math

number = int(input("Enter a number: "))

sqr_root = math.sqrt(number)
print(f"Square root of {number} is {sqr_root}")

log_root = math.log(number)
print(f"Log base of {number} is {log_root}")

sin_root = math.sin(number)
print(f"Sin root of {number} is {sin_root}")