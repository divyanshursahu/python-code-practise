#Exercise 1: Define a function that accepts 2 values and return its sum, subtraction and multiplication.

def calculator(a,b):

    sum = a+b
    
    if a > b:
        substract = a - b
    else:
        substract = b - a 

    mul = a * b
    print("The o/p is sum {0}, sub {1}, mul {2}".format(sum,substract, mul))

calculator(5,10)