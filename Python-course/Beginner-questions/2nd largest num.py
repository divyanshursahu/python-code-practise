# Question: Find the 2nd largest number in a list

# Solution:

def second_largest_num(list1):
    list1.sort(reverse = True)
    return list1[1]

list1 = [10, 5, 8, 20, 3]
print(second_largest_num(list1))