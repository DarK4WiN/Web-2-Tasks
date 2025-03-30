def length_of_string(string):
    count = 0
    for char in string:
        count += 1
    return count
string = input("Input string: ")
print(length_of_string(string))