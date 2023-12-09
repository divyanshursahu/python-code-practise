# Question: Write a Python program to find the factorial of a number.

# Solution:

import sys

def factorial(number):
    if number == 0:
        return 1
    else:
        fact = 1
        for i in range(1,number+1):
            fact = fact * i
    return fact

# User Input:
number = int(input("Enter the number you want to get the factorial for: "))
#number = 20

factorial = factorial(number)
print(f"The factorial of the {number} is: {factorial}")