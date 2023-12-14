def is_palindrome(input_string):
    normalized_string = input_string.lower().strip()
    reversed_string = normalized_string[::-1]

    return normalized_string == reversed_string


input_string1 = "malayalam"
print("Is", input_string1, "a palindrome?", is_palindrome(input_string1))


input_string3 = "hello"
print("Is", input_string3, "a palindrome?", is_palindrome(input_string3))
