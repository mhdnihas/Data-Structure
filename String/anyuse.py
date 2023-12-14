def replace_alphabets(input_string, n):
    alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
    shifted_alphabet_list = alphabet_list[n:] + alphabet_list[:n]
    output_string = ''

    for char in input_string:
        if char.isalpha():
            if char.islower():
                index = alphabet_list.index(char)
                output_string += shifted_alphabet_list[index]
            else:
                index = alphabet_list.index(char.lower())
                output_string += shifted_alphabet_list[index].upper()
        else:
            output_string += char

    return output_string


input_string1 = "hello"
n1 = 3
output_string1 = replace_alphabets(input_string1, n1)
print("Original string:", input_string1)
print("Shifted string:", output_string1)

input_string2 = "The123"
n2 = 13
output_string2 = replace_alphabets(input_string2, n2)
print("\nOriginal string:", input_string2)
print("Shifted string:", output_string2)


