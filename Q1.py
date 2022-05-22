# program to make a dictionary of alphabets and their ascii values

dictionary_of_ascii_alphabets = dict()

ascii_values = range(97,123)

for i in ascii_values:
    dictionary_of_ascii_alphabets[chr(i)] = i

print(dictionary_of_ascii_alphabets)



