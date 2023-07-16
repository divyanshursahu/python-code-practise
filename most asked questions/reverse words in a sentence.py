'''
Reverse words in a sentence
Problem Statement: Reverse the order of words in a given sentence.

Example: "sphinx of black quartz judge my vow" should output as "vow my judge quartz black of sphinx" '''

# def reverse(exm):
#     for i in exm:
#         i

exm = "sphinx of black quartz judge my vow"
split_exm = exm.split()
print("priting split string:", split_exm)
reverse_exm = split_exm[::-1]
print("Reverse string in list:", reverse_exm)
reversed_exm = " ".join(reverse_exm)
print(reversed_exm)
rev_string = []
new_string = []
for i in reverse_exm:
    rev_string = i[::-1]
    new_string.append(rev_string)
print(" ".join(new_string))
    



# exm = "sphinx of black quartz judge my vow"
# words = exm.split()
# print("printing splited string:" ,words)
# reversed_words = words[::-1]
# print("Printing revesed string",reversed_words)
# reversed_sentence = " ".join(reversed_words)
# print(reversed_sentence)