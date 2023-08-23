''' Problem Statement
Given an array of positive numbers ranging from 1 to n, such that all numbers from 1 to n are 
present except one number x, find x. Assume the input array is unsorted.
'''

def number(nums):
    total_len = len(nums) + 1
    total_sum = ( total_len * (total_len+1))//2

    for num in nums:
        total_sum = total_sum - num

    return total_sum


array1 = [3,6,5,7,8,9,2,1]
num = number(array1)
print("missing num:", num)
print("Old List", array1)  # actual program till here

array1.append(num)
print("new list",array1)
new_arr = []
new_arr += array1
print(new_arr)

# print(len(array1))

# array2 = sorted(array1)
# print(array2)


