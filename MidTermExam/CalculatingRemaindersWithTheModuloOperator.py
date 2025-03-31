def calculate_remainders(firstInput, secondInput):
    try:
        remainder = firstInput % secondInput
        print(f"The remainder of {firstInput} divided by {secondInput} is {remainder}")
    except ZeroDivisionError:
        print("Error: Can't divide by zero")
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
calculate_remainders(num1, num2)
