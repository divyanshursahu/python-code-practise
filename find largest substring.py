def largest_substring(str1,str2):
    
    max_length = 0
    newstr = ''
    for i in range(len(str1)):
        for j in range(len(str2)):
            length = 0
            while i + length < len(str1) and j + length < len(str2) and str1[i + length] == str2[j + length]:
                length += 1
            
            if length > max_length:
                max_length = length
                print(max_length)
                result = str1[i:i+length]
    return result

str1 = 'abcdefg'
str2 = 'defhgy'
result = largest_substring(str1,str2)
print("Result:", result)