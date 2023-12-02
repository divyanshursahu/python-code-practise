# Remove ''' from start and end to uncomment the code '''
''' def checkBalance(str1):
    count = 0
    ans = False

    if not str1:  # Check if the string is empty
        raise ValueError("Input string is empty")

    for i in str1:
        if i == "(" or i == "{" or i == "[":
            count += 1
        elif i == ")" or i == "}" or i == "]":
            count -= 1
        if count < 0:
            return ans

    if count == 0:
        return not ans

    return ans

try:
    str1 = input("Enter a string of brackets: ")
    print("Given string is balanced:", checkBalance(str1))
except ValueError as ve:
    print(f"Error: {ve}")  --> '''
# ----- Excluded the code below -------# 
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


# ----------- Program rewritten for practise using for loops --------- #

def checkbalanced(str1):
    if not str1:  # Check if the string is empty
        raise ValueError("Input string is empty")
    count = 0
    ans = False
    for i in str1:
        if i == '(' or i == '{' or i == '[':
            count += 1
        elif i == ')'  or i == '}' or i == ']':
            count -= 1
        if count < 0:
            return ans
    if count == 0:
        return not ans
    
    return ans

try:
    str1 = input("Enter the brackets to check:")
    print(f"ans:{checkbalanced(str1)}")
except ValueError as ve:
    print(f"Error: {ve}")



#str1 = input("Enter a string of brackets:")


