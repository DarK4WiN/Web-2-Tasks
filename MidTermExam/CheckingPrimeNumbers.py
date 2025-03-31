def is_prime(n):
    if n < 2 or n > 100:
        return False  # Numbers less than 2 or greater than 100 are not prime

    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
print(is_prime(number))