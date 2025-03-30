def absolute_value(num):
    if (num >= 0):
        return num
    else:
        return abs(num)
num = int(input("Input number: "))
print(absolute_value(num))
