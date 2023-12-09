# Question: Find the common elements between 2 lists

# solution:

def find_common_elements(list1, list2):
    common_list = []

# 1st logic   
    # for i in list1:
    #     for j in list2:
    #         if i == j:
    #             common_list.append(i)
    # return common_list

# 2nd logic
    for item in list1:
        if item in list2:
            common_list.append(item)
    return common_list        

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

common = find_common_elements(list1, list2)
print(common)