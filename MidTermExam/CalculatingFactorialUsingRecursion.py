def factorial(number):
    factorial = 1
    if number == 0:
        print("The factorial of 0 is 1")
    elif number > 0:
        while number > 1:
            factorial *= number
            number -= 1
        print(f"The factorial of {number} is {factorial}")
    else:
        print("Error: Number is negative")
number = int(input("Enter a number: "))
factorial(number)

