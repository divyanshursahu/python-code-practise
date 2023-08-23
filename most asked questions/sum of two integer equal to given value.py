''' 2. Determine if the sum of two integers is equal to a given value
Problem Statement: Given an array of integers and a value, determine if there are any two integers in the 
array whose sum is equal to the given value. 
Return true if the sum exists, and false if it does not. Consider the following array and its target sums:'''


def check_sum(num, val):
    check = False
    for s in range(0,len(num)):
        for v in range(1,len(num)):
            if num[s] + num[v] == val:
                check = True
                return check
    return check
            
arr = [5,7,1,2,8,4,3]
val = 19
print(check_sum(arr, val))

# def has_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return True
#     return False

# # Example usage
# arr = [1, 2, 4, 6, 3, 7, 8]
# target_sum = 19

# print(has_sum(arr, target_sum))  # True


