
# direct max function
'''
l = max(12,13,15)
print(l) '''

def max(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif a == b and b == c and c == a:
        print("All have same values")
    else:
        print(c)

#max(100,20,30)
v1 = int(input("Enter value 1:"))
v2 = int(input("Enter the value 2:"))
v3 = int(input("Enter the value 3:"))
max(v1,v2,v3)
