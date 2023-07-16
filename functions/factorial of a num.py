# Exercise 1: Write a program in Python to display the Factorial of a number.

'''Hint 1 
Input : 5

Expected output 
Factorial is 120

'''

# def factorial(num):
#     fact = 1
#     while num > 0:
#         fact = fact * num
#         print(num)
#         num -= 1
        
#     return(fact)    

# num = 4
# number=factorial(num)
# #number
# print(factorial(num))

def factorial(num):
    fact = 1
    for x in range(1,num+1):
       fact=fact*x
    return(fact)   

num = 4
number=factorial(num)
print(number)
#number
