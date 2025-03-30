def string_end_suffix(string, given_suffix):
    if string.endswith(given_suffix):
        return True
    else:
        return False
string = input("Input string: ")
given_character = input("Input character: ")
print(string_end_suffix(string, given_character))