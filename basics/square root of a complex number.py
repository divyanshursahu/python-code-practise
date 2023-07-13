# to calculate the square root of complex number

import cmath

#num = 1 + 2j
num = eval(input("enter the complex number:"))
square_rt = cmath.sqrt(num)
print(square_rt)


'''Note: If we want to take complex number as input directly, like 3+4j, we have to use the eval() function instead of float().

The eval() method can be used to convert complex numbers as input to the complex objects in Python.'''