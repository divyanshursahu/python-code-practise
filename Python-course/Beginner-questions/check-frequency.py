# Question: To count the frequency of each element in a list

# Solution:

def check_frequency(nums):
    temp = 0
    frequency = {}  # Initialize an empty dictionary to store the frequency of each number
    for num in nums:
        if num in frequency:
            frequency[num] += 1  # If the number is already in the dictionary, increment its frequency
        else:
            frequency[num] = 1   # If the number is not in the dictionary, add it with a frequency of 1
    return frequency  # Return the dictionary containing the frequency of each unique number

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
print(check_frequency(nums))
