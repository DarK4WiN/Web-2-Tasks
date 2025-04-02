def sum_of_digits(n):
    sum = 0
    n1 = n
    while n > 0:
        sum += n % 10
        n //= 10
    print(f"{n1} numbers sum of digits = {sum}")
n = int(input("Enter a number: "))
sum_of_digits(n)