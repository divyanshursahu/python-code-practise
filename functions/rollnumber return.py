# # Exercise 2: Define a function that accepts roll number and returns whether the student is present or absent.
'''
def roll_call(roll_list, usrin):
    for i in range(1,len(roll_list)):
        if i == usrin:
            print("Student Present")
            
        else:
            print("student absent")
            


roll_list = [12,13,14,16,1,2]
usrin = int(input("Enter the roll call to check:"))
roll_call(roll_list,usrin)

'''

# def process_list(my_list, user_input):
#     for item in my_list:
#         if item == user_input:
#             print("Match found!")
#             break

# my_list = [1, 2, 3, 4, 5]
# user_input = int(input("Enter a number: "))
# process_list(my_list, user_input)


# my_string = "Hello"
# for i in range(len(my_string)):
#   print (my_string)
#   my_string = 'a'

# my_string = "Hello World"
# i = "H"
# print(i)
# while i in my_string:
#   print(i)

i = 0
while i < 3:
  print(i)
  i++
  print i+1