# # 1st way by append function

# list1 = [10,20,30,40,50]
# list2 = []

# for n in list1:
#     list2.append(n * 2)

# print("list 1 {}:".format(list1))
# print("list 2 {}:".format(list2))

# # 2nd way without append

# list1 = [10,20,30,40,50]
# list2 = []

# for n in list1:
#     double = n * 2
#     list2 = list2 + [double]

# print("list 1 {}:".format(list1))
# print("list 2 {}:".format(list2))


nums = [10,20,30,40,50]
#nums_double = [ n * 2 for n in nums]  # without condition
nums_double = [n * 2 for n in nums if n % 4 == 0]
print(nums)
print(nums_double)