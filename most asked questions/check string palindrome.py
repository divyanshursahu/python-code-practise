# def palindrome(string):
#     reversed_string = string[::-1]
#     print(reversed_string)
#     if string == reversed_string:
#         print("Palindrome")
#     else:
#         print("Not palindrome")
    

# string = "poppop"
# palindrome(string)

def find_palindromic_substrings(string):
    results = []
    length = len(string)

    for i in range(length):
        for j in range(i+2, length+1):
            print(i)
            print(j)
    #         substring = string[i:j]
    #         if substring == substring[::-1]:
    #             results.append(substring)

    # return results

# Example usage:
string = "poppopo"
palindromic_substrings = find_palindromic_substrings(string)
print(palindromic_substrings)
