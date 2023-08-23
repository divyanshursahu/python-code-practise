# def steps(number):
#     n = number
#     m = 0
#     if n % 2 == 0 and n != 1:
#         n = n//2
#         m += 1
#     if n % 2 != 0 and n != 1:
#         n = (3 * n) +1
#         m += 1
#         print(m)
#         return m
#     return m

# steps(12)

def steps(number):
    count = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
            count += 1
        else:
            number = (number * 3) +1
            count += 1
    return count

s = steps(12)
print(s)

def steps(number):
    count = 0
    if number <= 0:
        raise ValueError("Only Positive integers are allowed")
    while number != 0:
        if number % 2 == 0:
            number /= 2
            count += 1
        else:
            number = (3 * number) + 1
            count += 1
        return(count)
            
    
    
        




