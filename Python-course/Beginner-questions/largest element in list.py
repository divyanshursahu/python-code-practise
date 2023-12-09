# Question : Write a Python program to find the largest element in a list.

# Solution 1: Using Max Function

#=============================
# num = [10,20,30,7,3]
# print(max(num))
#=============================

# Solution 2: using loops

def max_num(num_list):
    largest_num = num_list[0]
    for i in num_list:
        if i > largest_num:
            largest_num = i
            
    return largest_num

num_list = [10,20,30,7,3,30,31]
print(f"largest num : {max_num(num_list)}")



