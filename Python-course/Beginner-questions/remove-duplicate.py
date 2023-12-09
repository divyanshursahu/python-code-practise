# Question: Remove Duplicate from a list

# Solution

def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)

    return unique_nums


nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_duplicates(nums)

print(f"The list of unique nums: {unique_nums}")