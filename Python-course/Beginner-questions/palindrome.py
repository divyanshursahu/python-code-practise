#Question: Write a program to check if a string is a palindrome

# Program:

def check_palindrome(word):
    temp_word = ''
    temp_word = word[::-1]
    if word == temp_word:
        return True
    
    return False

word = str(input("Enter the word you want to check:"))
#word = "madam"
print(f"Is the word a palindrome: {check_palindrome(word)}")