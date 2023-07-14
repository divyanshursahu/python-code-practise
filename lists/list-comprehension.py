# nums = [10,20,30,40,50]
# #nums_double = [ n * 2 for n in nums]  # without condition
# nums_double = [n * 2 for n in nums if n % 4 == 0]
# print(nums)
# print(nums_double)

# list1 = [10,20,40,80,100]
# list2 = [30,60,90]

# sumlist = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]
# print(sumlist)

# list1 = [30, 50, 110, 40, 15, 75]
# list2 = [10, 60, 20, 50]

# sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

# print(sum_list)

string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
result = [len(s) for s in string_list if len(s) < 5]
print(result)