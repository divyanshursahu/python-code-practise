batman = "Bruce Wayne"

first = batman[0]  # Accessing the first character
print(first)

space = batman[5]  # Accessing the empty space in the string
print(space)

last = batman[len(batman) - 1]
print(last)
# The following will produce an error since the index is out of bounds
err = batman[len(batman)-1]
print(err)

print(len(batman))

str1 = "hello"
print(id(str1))

str1 = "bye"
print(id(str1))