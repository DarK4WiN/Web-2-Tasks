def calculate_power(numbers , exponent):
    for num in numbers:
        result =pow(num, exponent)
        print(f"{num} raised to the power of {exponent} is result {result}")

n = int(input("Input list length: "))
exponent_value = int(input("Input exponent value: "))
number_list = []
for num in range(n):
    number_list.append(int(input()))
calculate_power(number_list, exponent_value)

