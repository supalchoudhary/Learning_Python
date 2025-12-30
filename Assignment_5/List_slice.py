"""
Module 6: Data Structures and Strings in Python

Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

"""
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: ", ls)
print(f"Extracted first five elements: ", ls[0:5])

# Process 1: To print list in reverse order
# rev = ls[0:5]
# print(f"Reversed extracted elements: ", rev[::-1])

# Process:2 => Another way to print using index number
print(f"Reversed extracted elements: ", ls[ls.index(5)::-1])